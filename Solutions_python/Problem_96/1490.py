import sys

def main():
    test = sys.stdin.readline().lstrip()
    for num in xrange(int(test)):
        case = [int(i) for i in sys.stdin.readline().split()]
        ans = 0
        for person in xrange(case[0]):
            if (case[person+3]+2) / 3 >= case[2]:
                ans += 1
            elif (case[person+3]+4) / 3 >= case[2] and case[1] > 0 and case[person+3] >= 2:
                case[1] -= 1
                ans += 1
                 
        print "Case #%d: %d " % (num+1,ans)
    
if __name__ == "__main__":
    main()