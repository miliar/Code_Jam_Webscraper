T= int(input())
for j in range(T):
    num = input()
    max_c = '0'
    while(list(num)!=sorted(num)):
        for i, c in enumerate(num):
            if c>=max_c:
                max_c = c;
            else:
                num = num[:i]+"".join(('0' for i in range(len(num)-i)))
                num = int(num)-1
                num = str(num)
                break;
    print("Case #%s: %s"% (j+1, num))


