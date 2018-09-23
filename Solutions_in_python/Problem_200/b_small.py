def last_tid(num):
    lno = [int(j) for j in str(num)]
    if len(lno) < 2:
        return num
    i = 0
    repeat = -1
    while i < len(lno)-1:
        #print lno[i], lno[i+1], i
        if lno[i] <= lno[i+1]:
            if lno[i] == lno[i+1] and repeat == -1:
                repeat = i
            i = i+1
            continue
        else:
            break
        #i = i+1
    #print i,len(lno)-1
    if i == len(lno)-1:
        return num
    elif i == 0:
        #print num-1
        return last_tid(num-1)
    else:
        #print lno[i:]
        no = -1
        if repeat != -1:
            i = repeat
            #print i
            no = last_tid(int(''.join(map(str,lno[i:])))-1)
            #print no
            return no
        else:
            no = last_tid(int(''.join(map(str,lno[i:]))))
            lno_temp = [int(j) for j in str(no)]
            for j in range(len(lno_temp)):
                k = i+j
                lno[k] = lno_temp[j]
            return int(''.join(map(str,lno)))

def main():
    t = int(raw_input())
    for i in xrange(1, t+1):
        n = int(raw_input())
        ret = last_tid(n)
        print "Case #%d: %d" %(i,ret)

if __name__ == "__main__":
    main()