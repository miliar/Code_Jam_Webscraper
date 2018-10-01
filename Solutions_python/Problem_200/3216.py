import fileinput

pastFirstLine = False
caseNum = 0

def is_tidy(num):
    nums = list(str(num))
    i = 0
    currentMax = 0
    while i < len(nums):
        currentNum = int(nums[i])
        if currentNum >= currentMax:
            currentMax = currentNum
        else:
            return False
        i += 1
    return True

def decrease_num(num):
    nums = list(str(num))
    i = 1
    while i < len(nums):
        currentNum = int(nums[i])
        lastNum = int(nums[i - 1])
        if currentNum < lastNum:
            nums[i - 1] = str(lastNum - 1)
            while i < len(nums):
                nums[i] = "9"
                i += 1
        i += 1
    return int(''.join(nums))

for line in fileinput.input():
    if pastFirstLine:
        num = int(line)
        caseNum += 1
        while num > 0:
            if is_tidy(num):
                print "Case #" + str(caseNum) + ": " + str(num)
                break
            num = decrease_num(num)

    else:
        pastFirstLine = True
