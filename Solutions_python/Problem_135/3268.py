import sys


def check(l1, l2):
    pass


def main(f):
    num = f[0]
    output = []
    for case in range(int(num)):
        first_guess = int(f[case*10+1])
        #print first_guess
        pattern1 = f[case*10+2:case*10+6]
        #print pattern1
        second_guess = int(f[case*10+6])
        pattern2 = f[case*10+7:case*10+11]

        nums = pattern1[first_guess-1].strip().split()
        nums =[int(i) for i in nums]
        #print nums
        count = 0
        for num in pattern2[second_guess-1].strip().split():

            if int(num) in nums:
                res= "Case #%d: %d" %(case+1,int(num))
                #print res
                count+=1
        if count==0:
            print "Case #%d: Volunteer cheated!" %(case+1)
        elif count ==1:
            print res
        else:
            print "Case #%d: Bad magician!" %(case+1)


if __name__ == "__main__":
    f = list(open(sys.argv[1]))
    main(f)