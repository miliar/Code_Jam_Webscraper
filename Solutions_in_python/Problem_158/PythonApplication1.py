import sys

def main():
    YES = "GABRIEL"
    NO = "RICHARD"
    nums = [int(n) for n in raw_input().split(' ')]
    if nums[0] < 3:
        return YES if (nums[1]*nums[2])%nums[0] == 0 else NO
    elif nums[0] == 3:
        return YES if nums[1] != 1 and nums[2] != 1 and (nums[1]*nums[2])%nums[0] == 0 else NO
    else:
        return YES if (nums[1] == nums[0]-1  and nums[2] == nums[0]) or (nums[2] == nums[0]-1  and nums[1] == nums[0]) or (nums[2] == nums[1] == nums[0]) else NO

if __name__=="__main__":
    #sys.stdin = open("D-small-attempt0.in", "r")
    #sys.stdout = open("D-output.txt", "w")

    for n in xrange(input()):
        
        print "Case #%d: %s" % (n+1, main())
