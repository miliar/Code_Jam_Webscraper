num = [1,2,3,4,5,6,7,8,9]
last = [x for x in num]
tidies = [x for x in num]
m = 18

for mm in range(m-1):
    new = []
    for x in num:
        for tidy in last:
            s_tidy = str(tidy)
            if x <= int(s_tidy[0]):
                new.append(int(str(x) + s_tidy))
    last = new
    tidies.extend(last)
tidies.reverse()
import sys

n = (int) (sys.stdin.readline().strip())
for i in range (1, n+1):
    num = (int) (sys.stdin.readline().strip())
    for tidy in tidies:
        if tidy <= num:
            print(f"Case #{i}: {tidy}")
            break
