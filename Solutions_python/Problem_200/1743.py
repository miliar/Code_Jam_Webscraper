# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.

t = int(raw_input())  # read a line with a single integer

for i in xrange(1, t + 1):
#    line = raw_input().split()
#    flip_str = line[0]
#    pan = line[1]

    num_str = list(raw_input())

    if len(num_str) == 1:
        print "Case #"+str(i)+": "+"".join(num_str)
        continue

    index = 0

    for j in range(len(num_str)-1):
        if num_str[j] == num_str[j+1]:
            continue
        if num_str[j] > num_str[j+1]:
            break
        index = j+1
    if index != len(num_str)-1 and (num_str[index] != num_str[index+1] or num_str[-2] > num_str[-1]):
        num_str[index] = str(int(num_str[index])-1)
        for j in range(index+1, len(num_str)):
            num_str[j] = '9'
    num=int("".join(num_str))
    print "Case #"+str(i)+": "+str(num)
    