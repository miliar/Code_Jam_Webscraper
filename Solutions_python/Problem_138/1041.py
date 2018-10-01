T = int(input())
def war(n,k,N):
    k.sort()
    kent_score = 0
    naom_score = 0
    for naom in n:
        kent_flag = False
        for kent in k:
            kent_index = k.index(kent)
            if kent > naom:
                kent_score+=1
                kent_flag = True
                del k[kent_index]
                break
        if  kent_flag == False:
            del k[0]
            naom_score += 1
    return naom_score
    
def deceit_war(n,k,N):
    kent_score = 0
    naom_score = 0
    n.sort()
    k.sort()
    for naom in n:
        if naom > max(k):
            naom_score += len(k)
            break
        elif naom > min(k):
            naom_score += 1
            k.pop(0)
        else:
            k.pop()
            kent_score+=1
    return naom_score

for m in range(0,T):
    N = int(input())
    na = [float(x) for x in input().split(' ')]
    ke = [float(x) for x in input().split(' ')]
    y = deceit_war(na[:],ke[:],N)
    z =  war(na[:],ke[:],N)
    print("Case #" + str(m+1) + ':',  y , z)

