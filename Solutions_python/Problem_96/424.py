def solve():
    line=map(int,raw_input().split())

    n=line.pop(0)
    s=line.pop(0)
    p=line.pop(0)

    limit1=p*3-2 if p>=1 else p
    limit2=p*3-4 if p>=2 else p 

    number=0

    for sum_ in line:

        if sum_>=limit1 :

            number+=1

        elif sum_>=limit2 and s:

            s-=1 
            number+=1

    return number

cases=int(raw_input())

for i  in xrange(cases):
    print 'Case #{}: {}'.format(i+1,solve())
