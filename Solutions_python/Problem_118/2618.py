import math

def palendrome(num):
    if len(num) == 0:
        return True
    if num[0] == num[len(num) - 1]:
        return palendrome(num[1:len(num) - 1])
    else:
        return False

if __name__ == "__main__":

    input_file = open("C-small-attempt0.in", "r")
    case = int(input_file.readline())
    for case in range(0, case):
        line = input_file.readline()
        nums = line.split()
        i = 0
        count = 0
        for num in nums:
            nums[i] = int(num)
            i += 1
        for num in range(nums[0], nums[1] + 1):
            if palendrome(str(num)):
                rootnum = math.sqrt(num)
                if math.floor(rootnum) == rootnum:
                    rootnum = int(rootnum)
                    if palendrome(str(rootnum)):
                        count += 1
        print ("Case #%d: %d" %((case + 1), count))