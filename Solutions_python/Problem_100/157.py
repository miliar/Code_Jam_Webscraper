fin = open('B-small-attempt2.in','r')
fout = open('ansking.txt', 'w')

def second():
    global stars
    for i in range(len(sort2)):
        if haveComplete[sort2[i][2]] != 2:
            if sort2[i][1] <= stars:
                #print 'sort2', sort2[i]
                stars += 2 - haveComplete[sort2[i][2]]
                haveComplete[sort2[i][2]] = 2
                del(sort2[i])
                return 1
            else:
                return 0
    return 0
            
            
                
def first():
    global stars
    i = 0
    while i < len(sort1):
        if haveComplete[sort1[i][2]] == 2:
            del(sort1[i])
        else:
            if sort1[i][0] <= stars:
                #print 'sort1', sort1[i]
                stars += 1
                haveComplete[sort1[i][2]] = 1
                del(sort1[i])
                return 1
            else:
                return 0
    return 0
        

T = int(fin.readline())
for i in range(T):
    N = int(fin.readline())
    mas = []
    for j in range(N):
        a, b = map(int, fin.readline().split())
        mas.append((a,b,j))
    stars = 0
    sort1 = sorted(mas, key=lambda x: x[0] + 1-x[1]*0.00001)
    #print sort1
    sort2 = sorted(mas, key=lambda x: x[1])
    haveComplete = [0 for j in range(N)]
    cur1 = 0
    cur2 = 0
    steps = 0
    while 1:
        if second():
            steps += 1
        else:
            if first():
                steps += 1
            else:
                break
    
    good = 1
    for j in haveComplete:
        if j != 2:
            good = 0
            break
    print i, good, steps
    fout.write('Case #' + str(i+1) + ': ')
    if good:
        fout.write(str(steps) + '\n')
    else:
        fout.write('Too Bad\n')
    

    
fin.close()
fout.close()
