

def tidy(n):
    comp=-1
    aux=0
    while(n>0):
        aux=n%10
        if comp==-1:
            comp=aux
        elif aux>comp:
            return False
        comp=aux
        n=n//10
    return True

def solve(n):
    if tidy(n):
        return list(str(n))
    sn = list(str(n))
    sn[len(sn)-1]='0'
    for a in range(1,len(sn)):
        if sn[len(sn)-a-1]!='0':
            if len(sn)-a-1==0 and sn[len(sn)-a-1]=='1':
                sn.pop()
                for x in range(len(sn)):
                    sn[x]='9'
                return sn
            b = int(sn[len(sn)-a-1])-1
            sn[len(sn)-a-1]=str(b)
            aux = int(''.join(sn[0:len(sn)-a]))
            if not tidy(aux):
                continue
            for x in range(len(sn)-a, len(sn)):
                sn[x]='9'
            return sn
    return sn



i = int(input())
numbers = []
for a in range(i):
    s = numbers.append(int(input()))

res = "Case #%d: %s"

for a in range(i):
    print(res%(a+1, int(''.join(solve(numbers[a])))))