import math

f = open ('FairAndSquare.txt','r')
f1 = open ('OutFairAndSquare.txt','w')
cases = int(f.readline())
inp = f.read()
ranges = inp.split()

def pal (n):
    check = True
    mylist = list(n)
    mylist.reverse()
    word = (''.join(mylist))
    if word == n:
        return True
    else: return False

count = -2
for i in range(cases):
    total = 0
    count+=2
    ok = False
    for j in range(int(ranges[count]), int(ranges[count+1])+1):
        n = math.sqrt(j)
        n = (str(n).rstrip('0').rstrip('.'))
        ok = False
        try:
            int(n)
            ok = True            
        except ValueError:
            pass

        if ok == True:
            if pal(str(n)) == True and pal(str(j)) == True:
                total +=1

    print('Case #' + str(i+1) + ': ' + str(total), file =f1)


f1.close()
