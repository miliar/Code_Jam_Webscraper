import string
import re
import sys
input = open(sys.argv[1])
input_data = input.readline()
input_data=re.sub("\n","",input_data)


for i in range(0,int(input_data)):
	numero_eng = input.readline()
	numero_eng = re.sub("\n","",numero_eng)
	names_eng = range(0,int(numero_eng))
	for j in range(0,int(numero_eng)):
		names_eng[j] = input.readline()
		names_eng[j] = re.sub("\n","",names_eng[j])
	numero_que = input.readline()
	numero_que = re.sub("\n","",numero_que)
	querys = range(0,int(numero_que))
	for j in range(0,int(numero_que)):
		querys[j]= input.readline()
		querys[j]= re.sub("\n","",querys[j])
	switch=0
	blow=range(0,len(names_eng))
	for k in range(0,len(names_eng)):
		blow[k] = names_eng[k]
	first = 0
	for j in querys:
#		print(j)
#		print(blow)
		if (len(blow)==1) & (blow[0]==j):
			switch+=1
			blow=range(0,len(names_eng))
			for k in range(0,len(names_eng)):
				blow[k] = names_eng[k]
			blow.remove(j)
		else:
			try:
				blow.remove(j)
			except:
				blow = blow
	print('Case #'+str(i+1)+': '+str(switch))	
