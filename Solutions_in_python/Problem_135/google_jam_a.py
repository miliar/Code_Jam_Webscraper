import sys

def check_card(row1,cards1,row2,cards2):
    s1=set(cards1[row1-1])
    s2=set(cards2[row2-1])
    s=s1&s2
    if len(s1&s2)==0:
        result="Volunteer cheated!"
    elif len(s1&s2)==1:
        result=s.pop()
    else: result="Bad magician!"
    return result
        

with open('A-small-attempt0.in','r') as f:
	data=f.readlines()

N=int(data[0]);
res="";


for i in range(N):
    t=10*i
    row1=int(data[t+1])
    cards1=[_.split() for _ in data[t+2:t+6]]
    row2=int(data[t+6])
    cards2=[_.split() for _ in data[t+7:t+11]]
    res+="Case #"+str(i+1)+": "+check_card(row1,cards1,row2,cards2)+"\n"

#print res

with open('res.txt', 'w') as f:
	f.write(res)
