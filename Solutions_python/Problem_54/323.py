import fractions

def time(*nums):
    nums = sorted(nums)
    diffs = []
    for i in range(len(nums)-1):
        diffs.append(nums[i+1]-nums[i])
    gcf = diffs[0]
    for i in range(1, len(diffs)):
        gcf = fractions.gcd(gcf, diffs[i])
    if nums[0] % gcf == 0:
        return 0
    return gcf - (nums[0] % gcf)

with open("B-large.in") as fin:
    with open("B.out", "w") as fout:
        c = int(fin.readline())
        for i in range(1, c+1):
            s = fin.readline().split(" ")
            n = s[0]
            t = [int(n) for n in s[1:]]
            fout.write("Case #" + str(i) + ": " + str(time(*t)) + "\n")
            
