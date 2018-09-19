import sys

trdict={}
instr="zyqejp mysljylc kd kxveddknmc re jsicpdrysirbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcdde kr kd eoya kw aej tysr re ujdr lkgc jv"
trstr="qazour language is impossible to understandthere are twenty six factorial possibilitiesso it is okay if you want to just give up"
i=0
trdict[' ']=' '
trdict['\n']='\n'

for c in instr:
	trdict[c]=trstr[i]
	i+=1

#for c in range(97,123):
#	print("["+chr(c)+"]="+trdict[chr(c)]+";")

numlin=int(input())

for i in range(numlin):
	line=sys.stdin.readline()
	print("Case #"+str(i+1)+": ",end="")
	for c in line:
		print(trdict[c],end="")
	

