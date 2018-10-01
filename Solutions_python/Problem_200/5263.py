from sys import stdin
def solution(number,ordenado):
    order=[]
    for i in number:
        for j in i:
            order.append(j)
    a=sorted(order)
    if a==order:
        ordenado.append(number)   
def tidy():
    t=int(stdin.readline())
    c=1
    cases=t
    while cases!=0:
        l=int(stdin.readline())
        numbers= [str(x) for x in range(1,l+1)]
        ordenado=[]
        for i in range(len(numbers)):
            solution(numbers[i],ordenado)
        result=ordenado.pop()
        print('Case #'+str(c)+': '+str(result))
        c+=1
        cases-=1
tidy()

