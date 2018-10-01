t = int(input())

for ttt in range(t):
    print("Case #%d:" % (ttt+1), end=" ")
    n = int(input())
    A = input().split(" ")
    AA = []
    BB = []
    for ele in A:
        AA.append(float(ele))
    B = input().split(" ")
    for ele in B:
        BB.append(float(ele))
    AA = sorted(AA)
    BB = sorted(BB)
    CC = BB[:]
    wyn1 = 0
    wyn2 = 0
    for i in range(n):
        czy = 1
        for j in range(n):
            if AA[i] < BB[j]:
                BB[j] = 0.0
                czy = 0
                break
        if czy:
            wyn2 += 1
    for i in range(n):
        #print(AA, CC)
        if AA[0] < CC[0]:
            del(AA[0])
            del(CC[-1])
        else:
            wyn1 += 1
            del(AA[0])
            del(CC[0])
    print(wyn1, wyn2)