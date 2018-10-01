#!/usr/bin/python3

N = int(input())
for i in range(N):
    n1 = int(input())
    T1 = [list(map(int,input().split())) for i in range(4)]
    p1 = T1[n1-1]
    n2 = int(input())
    T2 = [list(map(int,input().split())) for i in range(4)]
    p2 = T2[n2-1]
    res = set(p2) & set(p1)
    
    string = (next(iter(res)) if len(res) == 1 else
              'Bad magician!' if len(res) > 1 else
              'Volunteer cheated!')
    print("Case #{}: {}".format(i+1,string))
        