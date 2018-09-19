def main():
    filename = 'A-large'
    
    inf = open(filename + '.in', 'r')
    outf = open(filename + '.out', 'w')
    for i, line in enumerate(inf):
        values = line.split()
        print values
        if i == 0:
            T = int(values[0]) # number of test cases
            print T
            continue
        if i <= T:
            N = int(values[0])
            R = [None]
            P = [None]
            for j in range(1, 2*N+1, 2):
                R.append(values[j])
                P.append(int(values[j+1]))
        else:
            continue
        
        print N, R, P
        
        time = 0
        posO = posB = 1
        next = 1
        
        print 'Time\tOrange\tBlue'
        while next <= N:
            time += 1
            cleared = False
            
            print time,
            
            # next button for orange robot
            try:
                nextO = P[next:][R[next:].index('O')]
#                print 'nextO: %d' % nextO
                if posO < nextO:
                    posO += 1
                    print '\tmove+',
                elif posO > nextO:
                    posO -= 1
                    print '\tmove-',
                else: # posO == nextO
                    if R[next] == 'O':
                        cleared = True
                        print '\tpush',
                    else:
                        pass # wait for blue robot
                        print '\tstay',
            except ValueError, e:
                print '\tgoal',
            
            try:
                # next button for blue robot
                nextB = P[next:][R[next:].index('B')]
#                print 'nextB: %d' % nextB
                if posB < nextB:
                    posB += 1
                    print '\tmove+'
                elif posB > nextB:
                    posB -= 1
                    print '\tmove-'
                else: # posB == nextB:
                    if R[next] == 'B':
                        cleared = True
                        print '\tpush'
                    else:
                        pass # wait for blue robot
                        print '\tstay'
            except ValueError, e:
                print '\tgoal'
            
            if cleared:
                next += 1
#            if time > 10000000:
#                break
        
        buf = 'Case #%d: %d\n' % (i, time)
        outf.write(buf)
    inf.close()


if __name__ == '__main__':
    main()
    
