import sys, time
def getArr ( num, a, b ):
    s = str(num)
    n = len(s)
    ds = s+s
    #arr = set([])
    arr= []
    for i in range ( 1, n ):
        #ss = s[i:]+s[0:i]
        ss = ds[i:i+n]
        if ss > s and ss <= b:
            if ss not in arr:
                arr.append(ss)
    return len(arr)

def main():
    beg = time.clock()
    f = open ('C-small-attempt0.in', 'r')
    ca = 1
    fw = open ( 'C-small-attempt0.out', 'w' )
    #T = int ( sys.stdin.next() )
    T = int ( f.readline() )
    while T:
        #line = sys.stdin.next().split()
        line = f.readline().split()
        a = int(line[0])
        b = int(line[1])
        n = 0
        arr = []
        for i in range ( a, b+1 ):
            n = n + getArr(i, str(a), str(b))
        T = T - 1;
        fw.write( 'Case #' + str(ca) + ": " + str(n)+'\n' )
        ca = ca + 1
    end = time.clock()    
    return end - beg
main()