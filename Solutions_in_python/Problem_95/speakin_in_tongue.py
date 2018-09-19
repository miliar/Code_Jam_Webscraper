#!/usr/bin/python
#Solution by Sajith Dilshan Edirisinghe
# email: sajithdilshan@gmail.com

text = 'ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv'
otxt = 'our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up'

dict={}
i=0
for item in text:
	dict[item] = otxt[i]
	i = i+1
dict['q']='z'
dict['z']='q'
dict['\n']=''

ins = open( "A-small-attempt0.in", "r" )
array = []
for line in ins:
    array.append( line )
array.pop(0)

list=[]
temp=''

for line in array:
	for letter in line:
		temp = temp + ''.join(dict[letter])
		#print dict[letter]
	list.append(temp)
	temp=''

file = open("output.txt","w")
i=1
for line in list:
	file.write("Case #"+str(i)+": "+line+"\n")
	i=i+1
file.close()
