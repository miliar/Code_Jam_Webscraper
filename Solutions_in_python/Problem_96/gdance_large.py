ifile = 'B-large.in'
ofile = 'B-large.out'

ifptr = open(ifile)
ofptr = open(ofile,'w')

N = int(ifptr.readline().rstrip()) #No. of test cases

for i in range(0,N):
    
    nums = [int(x) for x in ifptr.readline().rstrip().split()]

    n = 0
    s = nums[1] # surprizes
    p = nums[2] # high score
    t = nums[3:]# scores
    
    result = 0
    
    for score in t:
        
        if p == 0:
            result+=1
            continue
        elif score == 0:
            continue
        
        n+=1
        m = score / 3
        r = score % 3
        d = p - m
    
        if m >= p:
            result+=1
        elif d == 1 and r >= 1:
            result+=1
        elif d == 1 and r == 0 and s > 0:
            result+=1
            s-=1
        elif d == 2 and r == 2 and s > 0:
            result+=1
            s-=1
        else:
            print "Failed in Case %d THighScore:%d Person:%d/%d: SuprLeft:%d=> Total:%d" % (i+1, p, n, nums[0], s, score)
    
    ofptr.write("Case #%d: %d\n" % (i+1,result))

ifptr.close()
ofptr.close()