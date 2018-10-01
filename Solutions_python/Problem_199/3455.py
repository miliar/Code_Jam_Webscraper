#Oversized Pancake Flipper
#python3
#author: really

def flip(pan):
    s=''
    for i in range(len(pan)):
        s+= '+' if pan[i]=='-' else '-'
    return s

def gen(panc,k):
    s=[]
    for j in panc:
        for i in range(len(j)-k+1):
            s+=[(''.join([j[:i+0],flip(j[i:i+k]),j[i+k:]]))]
    return s

def solv(inp,k):
    k=int(k)
    li=[[inp]]
    c=0
    bfr=[[]]

    while not ('+'*len(inp)) in li[0]:
        li+=[list(set(gen(li[0],k)))]
        li.pop(0)
        c+=1
        if len(bfr)==len(li[0]) and not ('+'*len(inp)) in li[0]: return 'IMPOSSIBLE'
        bfr = li[0]
    return (str(c))

inn = int(input())
for i in range(inn):
    tmp=input()
    print('Case #'+str(i+1)+': '+(solv(tmp[:tmp.index(' ')],tmp[tmp.index(' ')+1:])))