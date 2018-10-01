def check(number):
    numb=str(number)
    llist=list(numb)
    for k in range(0,len(llist)-1):
        if int(llist[k])>int(llist[k+1]):
            return False
    return True


count=1

num=int(input())
for i in range(1, num+1):
    ip=int(input())
    for i in range(ip, 0, -1):
        result = check(i)
        if result == True:
            print("Case #{}: {}".format(count,i))
            count += 1
            break
