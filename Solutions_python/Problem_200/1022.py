f = open("B-large.in")
line = []
for l in f:
    line.append(l.strip())
c = 0
for num in line[1:]:
    c += 1
    for j in range(len(num) - 1):
        p = len(num) - 2 - j
##        print(num)
##        print(p)
        if int(num[p]) > int(num[p + 1]):
            num = num[0:p] + str(int(num[p]) - 1) + '9' * (len(num) - p - 1)
    if num[0] == '0':
        num = num[1:]
    print("Case #{}: {}".format(c, num))

  

