# Alien Language
# Greg Jackson
import re
def remove_values_from_list(the_list, val):
        while val in the_list:
            the_list.remove(val)
f = open('A-small-attempt1.in', 'r')
info = f.readline()
infolist=re.split(r'[\s]', str(info))
L=int(infolist[0])
D=int(infolist[1])
N=int(infolist[2])
dictionary=[]
test = []
for word in range(D):
    temp=list(str(f.readline()))
    temp.remove('\n')
    dictionary.append(temp)
for lol in range(N):
    temp = f.readline()
    templist=re.split(r'(\W)', str(temp))
    templist.insert(0,')')
    remove_values_from_list(templist, '')
    for i in range(len(templist)):
        if templist[i]==')':
            x=list(templist[i+1])
            x.reverse()
            for p in x:
                templist.insert(i+1, p)
            templist.pop(i+len(x)+1)
    remove_values_from_list(templist, ')')
    remove_values_from_list(templist, '(')
    remove_values_from_list(templist, '\n')
    test.append(templist)
f.close()
for case in test:
    for p in range(len(case)):
        case[p]=list(case[p])
count=1
file = open("output.txt","w")
for case in test:
        result=0
        for word in dictionary:
                check=0
                for i in range(L):
                        for p in case[i]:
                                if word[i]==p:
                                        check+=1
                if check==L:
                        result+=1
        print >>file, "Case #"+str(count)+":", result
        count+=1
file.close()
                        
                

        
