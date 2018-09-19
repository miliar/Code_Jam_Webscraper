import fileinput as FI

def main():
    inPut = FI.input()
    cases = int(inPut.readline())
    for case in xrange(cases):
        [R, C, W] = inPut.readline().split()
        R = int(R)
        C = int(C)
        W = int(W)
        X = 0
        if C == W:
            y = R + W-1
        elif W == 1:
            y = R*C
        else:
            for i in range(0, C, W):
                X +=1
            y = X * R + (W - 1)
        print 'Case #'+ str(case+1) + ': '+ str(y)
        
if __name__ == "__main__":
    main()