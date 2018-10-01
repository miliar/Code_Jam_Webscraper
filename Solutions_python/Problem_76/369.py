n=input()
for case in range(n):
    input()
    nums=sorted(int(x) for x in raw_input().split())
    if reduce(int.__xor__, nums):
        res="NO"
    else:
        for i in range(1,len(nums)):
            lhs, rhs = nums[:i], nums[i:]
            if reduce(int.__xor__,lhs) == reduce(int.__xor__,rhs):
                res = sum(rhs)
                break

    print "Case #%s:"%(case+1), res
