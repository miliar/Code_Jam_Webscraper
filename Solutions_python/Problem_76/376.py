import sys

sys.stdin = open("C:\\Users\\Kuldeep\\Downloads\\C-large.in")
sys.stdout = open("C:\\Users\\Kuldeep\\Desktop\\out.txt",'w')

t = int(raw_input())

for x in range(t):
    n = int(raw_input())
    s = 0
    l = map(int,raw_input().split())
    xor = 0
    mini = 1<<30
    for i in range(n):
        xor^=l[i]
        s+=l[i]
        mini = min(mini,l[i])
    if xor == 0:
        ans = s - mini
    else:
        ans = 'NO'
    sys.stdout.write("Case #"+str(x+1)+": ")
    print ans