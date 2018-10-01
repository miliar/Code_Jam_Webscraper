def check(n):
    val = 1
    for i in range(len(n)-1):
        if int(n[i]) <= int(n[i+1]):
            val = 1
            #print(val,n)
        else:
            val = 0
            #print(val,n)
            break
    if val == 1:
        return n
    else:
        #print(n)
        return check(str(int(n)-1))

t = int(input())
for _ in range(t):
    n = input()
    x=check(n)
    with open('notepad.txt', 'a') as fout:
        fout.write('Case #')
        fout.write(str(_+1))
        fout.write(': ')
        fout.write(str(x))
        fout.write('\n')