def sol2(num_,num_sup, p, scorelist):
    l = []
    ret = 0
    count  = num_sup
    for i in scorelist:
        l.append(int(i))
        
    l.sort()
    l.reverse()

    for i in l:
        if i >= p * 3:
            ret +=1
        else:
            break

    l = l[ret:]

    
    for i in l:
        if i+2 >= p * 3:
            ret += 1
        elif i > p and count > 0 and i+4 >= p * 3:
            ret += 1
            count -= 1
    
    return ret


if __name__ == '__main__':
    f = open("B-small-attempt2.in",'r')
    num = f.readline()
    
    t = open('output.txt','w')
    
    for i in range(int(num)):
        line = f.readline()
        l = line.strip().split()

        N = l[0]
        s = l[1]
        p = l[2]

        t.write("Case #" + str(i+1) + ": " + str(sol2(int(N),int(s),int(p),l[3:])) + "\n")
        
    f.close()
    t.close()