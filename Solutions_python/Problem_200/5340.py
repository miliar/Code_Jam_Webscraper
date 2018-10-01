def areSorted(n):
    next_digit=n%10
    n=int(n/10)
    while n:
        digit=n%10
        if digit > next_digit:
            return False
        next_digit=digit
        n=int(n/10)
    return True
for j in range(int(input())):
    n=int(input())
    for i in range(n,0,-1):
        if areSorted(i):
            print("Case #%d: %d" % (j+1,i))
            break
    
