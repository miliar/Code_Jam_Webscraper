import sys

samples_i=['ejp mysljylc kd kxveddknmc re jsicpdrysi','rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd','de kr kd eoya kw aej tysr re ujdr lkgc jv']
samples_o=['our language is impossible to understand','there are twenty six factorial possibilities','so it is okay if you want to just give up']

d={'y':'a','e':'o','q':'z'}

for i in range(len(samples_i)):
	for j in range(len(samples_i[i])):
		cc=samples_o[i][j]#corresponding character
		if samples_i[i][j] in d:#just to make sure
			if cc!=d[samples_i[i][j]]:
				print('Error!','i=%d,j=%d'%(i,j))
				sys.exit()
		d[samples_i[i][j]]=samples_o[i][j]

inl=d.keys()#input letters
opl=d.values()#output letters
nii=[]#not in input
nio=[]#not in output
for i in range(97,123):
	if chr(i) not in inl:
		nii+=[chr(i)]
	if chr(i) not in opl:
		nio+=[chr(i)]

if len(nii)==len(nio)==1:
	d[nii[0]]=nio[0]

file=open('problem 1-dict','w')
file.write(repr(d))
file.close()