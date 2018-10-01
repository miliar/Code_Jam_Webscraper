

def direct():

    f = open("A-large.in", "r")
    #f = open("input", "r")
    T = int(f.readline())

    for testNum in xrange(1, T+1):

        N, M = map(int, f.readline().split())

        computer = set()

        for _ in range(N):
            computer.add(f.readline().strip())
            
        needed = 0

        for _ in range(M):
            want = f.readline().strip()

            while True:
                
                if want in computer or want == '':
                    break
                needed += 1

                computer.add(want)
                want = want.rsplit("/", 1)[0]       

        print "Case #%d: %d" % (testNum, needed)
        
direct()
