def main():
    T = int(raw_input())
    for t in xrange(1,T+1):
        r = int(raw_input())-1
        s1 = set()
        for n in xrange(4):
            l = raw_input()
            if n == r:
                row = map(int,l.split())
                for e in row:
                    s1.add( e )
        
        r = int(raw_input())-1
        s2 = set()
        for n in xrange(4):
            l = raw_input()
            if n == r:
                row = map(int,l.split())
                for e in row:
                    s2.add( e )

        s3 = s1 & s2
        
        print "Case #"+str(t)+":",
        if len(s3) > 1:
            print "Bad magician!"
        elif len(s3) == 0:
            print "Volunteer cheated!"
        else:
            print list(s3)[0]

if __name__ == "__main__":
    main()
