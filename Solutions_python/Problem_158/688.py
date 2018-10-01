t = int(input())

for i in range(t):

    q = input().split()
    n = int(q[0])
    l = int(q[1])
    b = int(q[2])

    if(n == 1):
        ans = 'GABRIEL'
    elif(n == 2):
        if((l*b) % 2 == 0):
            ans = 'GABRIEL'
        else:
            ans = 'RICHARD'
    elif(n == 3):
        if((l*b) % 3 != 0 or (l == 3 and b == 1) or (l == 1 and b == 3)):
            ans = 'RICHARD'
        else:
            ans = 'GABRIEL'
    elif(n == 4):
        if((l*b) % 4 != 0 or (l == 2 and b == 2) or (l == 4 and b == 1) or (l == 1 and b == 4) or (l == 2 and b == 4) or (l == 4 and b == 2)):
            ans = 'RICHARD'
        else:
            ans = 'GABRIEL'

    print("Case #" + str(i+1) + ": " + ans)
