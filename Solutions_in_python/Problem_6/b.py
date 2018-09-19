import decimal
D = decimal.Decimal
decimal.getcontext().prec = 3000
a = D(3) + D(D.sqrt(D(5)))
t = int(raw_input())
for cn in range(t):
    q = int(raw_input())
    b = pow(a,q)
    ans = str(b)
    f = ans.find('.')
    ans = ans[max([f-3,0]):f]
    while len(ans) < 3:
        ans = '0' + ans
    print "Case #" + str(cn+1) + ": " + ans
