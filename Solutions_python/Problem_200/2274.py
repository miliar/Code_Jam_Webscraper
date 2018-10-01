def tidy(nums):
    nums = list(nums.strip())
    p = i = 0
    while i < len(nums) - 1:
        left, right = int(nums[i]), int(nums[i + 1])
        if left < right:
            p = i + 1
        elif left > right:
            nums[p] = str(int(nums[p]) - 1)
            p += 1
            while p < len(nums):
                nums[p] = "9"
                p += 1
        i += 1
    return nums

fin = open("B-large.in", "r")
fout = open("output", "w")

i = 1
cases = fin.readlines()
while i < len(cases):
    case = cases[i]
    fout.write("Case #" + str(i) + ": "+ str(int("".join(tidy(case)))) + "\n")
    i += 1
fout.close()
fin.close()

