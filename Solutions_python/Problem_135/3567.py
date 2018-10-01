

def f1():
	temp1=[];temp2=[]
	num1=int(raw_input())
	for i in xrange(0,4):
		l1=raw_input().split(' ')
		l1=[int(x.strip()) for x in l1]
		temp1.append(l1)
	num2=int(raw_input())
	for i in xrange(0,4):
		l1=raw_input().split(' ')
		l1=[int(x.strip()) for x in l1]
		temp2.append(l1)
	return temp1[num1-1],temp2[num2-1]


def f2(retlist1,retlist2,i):
	count=0
	num=-1
	#import pdb;pdb.set_trace()
	for x in retlist1:
		for y in retlist2:
			if x==y:
				count=count+1
				num=x
			if count>=2:
				break
		if count>=2:
			break
	if count>=2:
		return 'Case #%d: Bad magician!'%(i+1)
	elif count==0:
		return 'Case #%d: Volunteer cheated!'%(i+1)
	elif count==1:
		return 'Case #%d: %d'%(i+1,num)


if __name__=="__main__":
	n=int(raw_input())
	elemdict={}
	for i in xrange(0,n):
		retlist1,retlist2=f1()
		elemdict[i]={'list1':retlist1,'list2':retlist2}
	for i in xrange(0,n):
		print f2(elemdict[i]['list1'],elemdict[i]['list2'],i)

	