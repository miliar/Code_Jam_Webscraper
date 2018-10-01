input = open('C-large.in', 'r')
output = open('C-large.out', 'w')
t = int(input.readline().rstrip())
for test in range(t):
    output.write("Case #" + str(test + 1) + ": ")
    n, k = map(int, input.readline().rstrip().split())
    lengs = [n]
    nums = [1]
    while k > nums[0]:
        k -= nums[0]
        len_new = lengs[0] - 1 - (lengs[0] - 1) // 2
        if len_new in lengs:
            nums[lengs.index(len_new)] += nums[0]
        else:
            lengs.append(len_new)
            nums.append(nums[0])
        len_new = (lengs[0] - 1) // 2
        if len_new in lengs:
            nums[lengs.index(len_new)] += nums[0]
        else:
            lengs.append(len_new)
            nums.append(nums[0])
        lengs.pop(0)
        nums.pop(0)
    print(lengs[0] - 1 - (lengs[0] - 1) // 2, (lengs[0] - 1) // 2, file = output)

input.close()
output.close()