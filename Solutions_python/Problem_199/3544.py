def flip(b, start, end):
    #b = b[::-1]
    global count
    count += 1
    b = list(b)
    #print b[start:end]
    for i in xrange(start, end):
        #print i
        if b[i] == '+':
            b[i] = '-'
        else:
            b[i] = '+'
    b = "".join(b)
    #print b
    return b

def main():
    n = int(raw_input())
    for j in xrange(n):
        a = raw_input()
        b = a.split(' ')
        a = b[0]
        flipper = int(b[1])
        global count
        count = 0
        if len(a) < flipper:
            print "Case #%d: %s" % (j+1, "IMPOSSIBLE")
            break
        else:
            #print a
            #print flipper
            end = len(a) - flipper
            for i in xrange(end+1):
                #print i
                #print a[i]
                if a[i] == '-':
                    #print i
                    #print "FLIPPER"
                    a = flip(a, i, i+flipper)
                    #print a
                else:
                    continue
        #print a
        a = list(a)
        if '-' in a:
            print "Case #%d: %s" % (j+1, "IMPOSSIBLE")
        else:
            print "Case #%d: %d" % (j+1, count) 
        #print count

count = 0
main()
