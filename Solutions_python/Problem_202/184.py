# -*- coding: utf-8 -*-
"""
Created on Fri Apr  7 18:59:29 2017

@author: adobe
"""
import numpy as np
import copy
magic = lambda nums: int(''.join(str(i) for i in nums))
from math import *
N=input()
ans=[]
mats=[]
scores=[]
oo=ord('o')
ox=ord('x')
op=ord('+')

def embed(mat):
	D=mat.shape[0]
	n=2*D-1
	res=np.zeros([n,n])
	for r in range(D):
		for c in range(D):
			res[r+c,D-1-r+c]=mat[r,c]
	return res

def antiembed(mat):
	D=mat.shape[1]
	n=(D+1)/2
	res=np.zeros([n,n])
	for r in range(n):
		for c in range(n):
			res[r,c]=mat[r+c,n-1-r+c]
	return res

def tri(mat):
	D=mat.shape[0]
	trir=np.zeros([2*D-1,D])
	trir-=1
	for tmp in range(D):
		for tmp2 in range(tmp+1):
			rt=tmp-tmp2
			ct=tmp2
			trir[tmp,tmp2]=mat[rt,ct]
	for tmp in range(D,2*D-1):
		for tmp2 in range(tmp-D+1,D):
			rt=tmp-tmp2
			ct=tmp2
			trir[tmp,tmp2-tmp-1+D]=mat[rt,ct]
	return trir


def antitri(mat):
	D=mat.shape[1]
	trir=np.zeros([D,D])
	for tmp in range(D):
		for tmp2 in range(tmp+1):
			rt=tmp-tmp2
			ct=tmp2
			trir[rt,ct]=mat[tmp,tmp2]
	for tmp in range(D,2*D-1):
		for tmp2 in range(tmp-D+1,D):
			rt=tmp-tmp2
			ct=tmp2
			trir[rt,ct]=mat[tmp,tmp2-tmp-1+D]
	return trir


def rank(mat):
	d=len(mat)
	dec=np.zeros([d,d])
	csum=np.sum(mat,axis=0)
	rsum=np.sum(mat,axis=1)
	rsofcsum=np.repeat(np.matrix(csum),d,axis=0)
	csofrsum=np.repeat(np.matrix(rsum).T,d,axis=1)
	### print rsofcsum
	### print csofrsum
	end=csofrsum+rsofcsum
	### print end
	end=np.multiply(end,mat)
	### print end
	ranks=np.argsort(end.flatten())
	### print ranks
	for i in range(ranks.shape[1]):
		r=int(ranks[0,i]/d)
		c=int(ranks[0,i]%d)
		if end[r,c]!=0:
			dec[r,c]=1
			end[r,:]=0
			end[:,c]=0
	### print dec
	return dec

def gradep(mat):
	d=len(mat)
	dec=np.zeros([d,d])
	csum=np.sum(mat,axis=0)
	rsum=np.sum(mat,axis=1)
	rsofcsum=np.repeat(np.matrix(csum),d,axis=0)
	csofrsum=np.repeat(np.matrix(rsum).T,d,axis=1)
	### print rsofcsum
	### print csofrsum
	end=csofrsum+rsofcsum
	### print end
	end=np.multiply(end,mat)
	return end

def gradex(matt):
	#before diamond shape
	mat=embed(matt)
	d=len(mat)
	dec=np.zeros([d,d])
	csum=np.sum(mat,axis=0)
	rsum=np.sum(mat,axis=1)
	rsofcsum=np.repeat(np.matrix(csum),d,axis=0)
	csofrsum=np.repeat(np.matrix(rsum).T,d,axis=1)
	### print rsofcsum
	### print csofrsum
	end=csofrsum+rsofcsum
	### print end
	end=np.multiply(end,mat)
	ret=antiembed(end)
	return np.matrix(ret)


def togetherrank(x,p,M,sub):
	#!!!make sure M is changed globally !!!!!!!!!!
	#return current line answer
	extrascore=0
	lines=[]
	d=M.shape[1]
	scorex=gradex(x)
	scorep=gradep(p)
	scorexp=np.concatenate((scorex.flatten(),scorep.flatten()),axis=1)
	scorexp=np.array(scorexp)[0]
	lengthtot=len(scorexp)
	lengthsing=int(lengthtot/2)

	ranktot=np.matrix(np.argsort(scorexp))
	### print ranks
	for ii in range(ranktot.shape[1]):
		i=ranktot[0,ii]
		if i<lengthsing:
			#x grade
			#put p
			#update mat, record change to answers, delete diags in x grade, delete point in p grade
			r = int(i/d)
			c = i%d
			#print r,c
			if x[r,c]==0:
				continue
			M[r,c]=op
			extrascore+=1
			sub[r,c]=len(lines)
			lines.append("+ "+str(r+1)+" "+str(c+1))
			nr=r
			nc=c
			while nr<d-1 and nc<d-1:
				nr+=1
				nc+=1
				x[nr,nc]=0
			nr=r
			nc=c
			while nr<d-1 and nc>=1:
				nr+=1
				nc-=1
				x[nr,nc]=0
			nr=r
			nc=c
			while nr>0 and nc<d-1:
				nr-=1
				nc+=1
				x[nr,nc]=0
			nr=r
			nc=c
			while nr>0 and nc>0:
				nr-=1
				nc-=1
				x[nr,nc]=0
			p[r,c]=0
		else:
			#p
			#update mat, record change to answers, delete diags in p grade, delete point in x grade
			i-=lengthsing
			r = int(i/d)
			c = i%d
			#print r,c
			if p[r,c]==0:
				continue
			M[r,c]=ox
			extrascore+=1
			sub[r,c]=len(lines)
			lines.append("x "+str(r+1)+" "+str(c+1))
			nr=r
			nc=c
			p[r,:]*=0
			p[:,c]*=0
			x[r,c]=0

	return (extrascore,len(lines),lines)

	### print dec

def orank(x,p,M,sub,curlines):
	#!!!make sure M is changed globally !!!!!!!!!!
	#return current line answer
	#x oo from ox check op on diags
	#p oo from op check ox on row cols
	extrascore=0
	lines=[]
	d=M.shape[1]
	scorex=gradex(x)
	scorep=gradep(p)
	scorexp=np.concatenate((scorex.flatten(),scorep.flatten()),axis=1)
	scorexp=np.array(scorexp)[0]
	lengthtot=len(scorexp)
	lengthsing=int(lengthtot/2)

	ranktot=np.matrix(np.argsort(scorexp))
	### print ranks
	for ii in range(ranktot.shape[1]):
		i=ranktot[0,ii]
		if i<lengthsing:	
			#x grade
			#put p
			#update mat, record change to answers, delete diags in x grade, delete point in p grade
			r = int(i/d)
			c = i%d
			#print r,c
			if x[r,c]==0:
				continue
			
			M[r,c]=oo
			extrascore+=1
			ind=int(sub[r,c])
			if ind==-1:
				lines.append("o "+str(r+1)+" "+str(c+1))
			else:
				curlines[ind]="o "+str(r+1)+" "+str(c+1)

			nr=r
			nc=c
			while nr<d-1 and nc<d-1:
				nr+=1
				nc+=1
				x[nr,nc]=0
			nr=r
			nc=c
			while nr<d-1 and nc>=1:
				nr+=1
				nc-=1
				x[nr,nc]=0
			nr=r
			nc=c
			while nr>0 and nc<d-1:
				nr-=1
				nc+=1
				x[nr,nc]=0
			nr=r
			nc=c
			while nr>0 and nc>0:
				nr-=1
				nc-=1
				x[nr,nc]=0
			p[r,c]=0
		else:
			#p
			#update mat, record change to answers, delete diags in p grade, delete point in x grade
			i-=lengthsing
			r = int(i/d)
			c = i%d
			#print r,c
			if p[r,c]==0:
				continue

			M[r,c]=oo
			extrascore+=1
			ind=int(sub[r,c])
			if ind==-1:
				lines.append("o "+str(r+1)+" "+str(c+1))
			else:
				curlines[ind]="o "+str(r+1)+" "+str(c+1)
			nr=r
			nc=c
			p[r,:]*=0
			p[:,c]*=0
			x[r,c]=0

	return (extrascore,len(lines),lines)




# t=np.array([[ 1.,  1.,  1.],
#        [ 0.,  0.,  0.],
#        [ 1.,  0.,  1.]])
## # print rank(t)
## print gradex(t)
## print gradep(t)

# tp=np.array([[ 0.,  0.,  0.],
#        [ 0.,  0.,  0.],
#        [ 0.,  1.,  0.]])
# tx=np.array([[ 0.,  0.,  0.],
#        [ 1.,  1.,  1.],
#        [ 1.,  1.,  1.]])
## # print rank(t)
## print gradex(t)
## print gradep(t)



for i in range(N):
	sen=raw_input()
	(D,num)=sen.split()
	D=int(D)
	num=int(num)
	mat=np.zeros([D,D])
	curans=[]
	curscore=0

	for ii in range(num):
		senn=raw_input()
		(con,row,col)=senn.split(' ')
		row=int(row)
		col=int(col)
		row-=1
		col-=1
		mat[row,col]=ord(con)
		if con=='+' or con=='x':
			curscore+=1
		elif con=='o':
			curscore+=2
		else:
			input("FAULT HERE!!! con is not one of three")
	
	##print "mat0\n",mat

	subsub=-np.ones([D,D])

	######## ox
	ravails=np.zeros([D,D])
	for r in range(D):
		can=True
		avails=np.zeros(D)
		for c in range(D):
			if mat[r,c]==oo or mat[r,c]==ox:
				can=False
			elif mat[r,c]==0:
				avails[c]=1
			
		if can==True:
			ravails[r]=avails

	cavails=np.zeros([D,D])
	for c in range(D):
		can=True
		avails=np.zeros(D).T
		for r in range(D):
			if mat[r,c]==oo or mat[r,c]==ox:
				can=False
			elif mat[r,c]==0:
				avails[r]=1
			
		if can==True:
			cavails[:,c]=avails

	allavails=np.multiply(ravails,cavails)
	oxavails=copy.copy(allavails)
	# dec=rank(allavails)
	# mat+=dec*ox
	# nonzerox=dec.nonzero()[0]
	# nonzeroy=dec.nonzero()[1]
	# for tmp in range(len(nonzerox)):
	# 	curans.append("x "+str(nonzerox[tmp]+1)+" "+str(nonzeroy[tmp]+1))
	# curscore+=sum(sum(dec))
	
	##print "mat ox\n",mat


	
	################  op
	##(1,1)

	tri1=tri(mat)
	#2*d-1*d
	ravails=np.zeros([2*D-1,D])
	for r in range(2*D-1):
		can=True
		avails=np.zeros(D)
		for c in range(D):
			if tri1[r,c]==oo or tri1[r,c]==op:
				can=False
			elif tri1[r,c]==0:
				avails[c]=1
			
		if can==True:
			ravails[r]=avails

	rback1=antitri(ravails)


	tri2=tri(np.rot90(mat))
	#2*d-1*d
	ravails=np.zeros([2*D-1,D])
	for r in range(2*D-1):
		can=True
		avails=np.zeros(D)
		for c in range(D):
			if tri2[r,c]==oo or tri2[r,c]==op:
				can=False
			elif tri2[r,c]==0:
				avails[c]=1
			
		if can==True:
			ravails[r]=avails

	rback2=np.rot90(antitri(ravails),3)



	# temp=np.multiply(rback1,rback2)
	opavails=np.multiply(rback1,rback2)

	(extrascore,numlines,lines)=togetherrank(x=opavails,p=oxavails,M=mat,sub=subsub)
	curscore+=extrascore
	curans+=copy.copy(lines)
	#print "after together rank"
	#print extrascore
	#print numlines
	#print lines


	# allsavails=embed(temp)
	

	# sdec=rank(allsavails)
	# dec=antiembed(sdec)







	##print "dec for op:"
	##print dec

	# dec=np.zeros([D,D])
	# for r in range(D):
	# 	for c in range(D):
	# 		(row,col)=r*np.array([1,1])+c*np.array([-1,1])
	# 		row=(row+D)%D
	# 		col=(col+D)%D
	### 		# print (row,col)
	# 		dec[row,col]=sdec[r,c]
	

	# mat+=dec*op
	# nonzerox=dec.nonzero()[0]
	# nonzeroy=dec.nonzero()[1]
	# for tmp in range(len(nonzerox)):
	# 	curans.append("+ "+str(nonzerox[tmp]+1)+" "+str(nonzeroy[tmp]+1))
	# curscore+=sum(sum(dec))


	##print "mat op\n",mat




	#########################   oo

	ravails=np.zeros([D,D])
	for r in range(D):
		can=True
		avails=np.zeros(D)
		for c in range(D):
			if mat[r,c]==ox or mat[r,c]==oo:
				can=False
			elif mat[r,c]==op:
				avails[c]=1
			
		if can==True:
			ravails[r]=avails

	cavails=np.zeros([D,D])
	for c in range(D):
		can=True
		avails=np.zeros(D).T
		for r in range(D):
			if mat[r,c]==ox or mat[r,c]==oo:
				can=False
			elif mat[r,c]==op:
				avails[r]=1
			
		if can==True:
			cavails[:,c]=avails

	

	ooopavails=np.multiply(ravails,cavails)
	#oo from op check ox on rows cols
	# allavails=np.multiply(ravails,cavails)
	

	# dec=rank(allavails)
	# mat+=dec*(oo-op)
	# nonzerox=dec.nonzero()[0]
	# nonzeroy=dec.nonzero()[1]
	# for tmp in range(len(nonzerox)):
	# 	curans.append("o "+str(nonzerox[tmp]+1)+" "+str(nonzeroy[tmp]+1))
	# curscore+=sum(sum(dec))
	##print "mat oo from op\n",mat








	tri1=tri(mat)
	#2*d-1*d
	ravails=np.zeros([2*D-1,D])
	for r in range(2*D-1):
		can=True
		avails=np.zeros(D)
		for c in range(D):
			if tri1[r,c]==op or tri1[r,c]==oo:
				can=False
			elif tri1[r,c]==ox:
				avails[c]=1
			
		if can==True:
			ravails[r]=avails

	rback1=antitri(ravails)


	tri2=tri(np.rot90(mat))
	#2*d-1*d
	ravails=np.zeros([2*D-1,D])
	for r in range(2*D-1):
		can=True
		avails=np.zeros(D)
		for c in range(D):
			if tri2[r,c]==op or tri2[r,c]==oo:
				can=False
			elif tri2[r,c]==ox:
				avails[c]=1
			
		if can==True:
			ravails[r]=avails

	rback2=np.rot90(antitri(ravails),3)



	oooxavails=np.multiply(rback1,rback2)
	(extrascore,numlines,lines)=orank(p=ooopavails,x=oooxavails,M=mat,sub=subsub,curlines=curans)
	curscore+=extrascore
	curans+=copy.copy(lines)
	# temp=np.multiply(rback1,rback2)
	# allsavails=embed(temp)
	# sdec=rank(allsavails)
	# dec=antiembed(sdec)
	##print "dec for op:"
	##print dec

	# dec=np.zeros([D,D])
	# for r in range(D):
	# 	for c in range(D):
	# 		(row,col)=r*np.array([1,1])+c*np.array([-1,1])
	# 		row=(row+D)%D
	# 		col=(col+D)%D
	### 		# print (row,col)
	# 		dec[row,col]=sdec[r,c]
	# mat+=dec*(oo-ox)
	# nonzerox=dec.nonzero()[0]
	# nonzeroy=dec.nonzero()[1]
	# for tmp in range(len(nonzerox)):
	# 	curans.append("o "+str(nonzerox[tmp]+1)+" "+str(nonzeroy[tmp]+1))
	# curscore+=sum(sum(dec))
	##print "mat oo from ox\n",mat




	ans.append(copy.copy(curans))
	scores.append(int(curscore))
	## print mat
	# mats.append(copy.copy(mat))
### print ans
f = open('tryD.out', 'w')

for j,con in enumerate(ans):
	# print "Case #"+str(j+1)+": "+str(scores[j])+" "+str(len(con))
	# for jj in con:
		# print jj
	print >>f,"Case #"+str(j+1)+": "+str(scores[j])+" "+str(len(con))
	for jj in con:
		print >>f,jj


f.close()