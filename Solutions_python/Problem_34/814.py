# Usage:
# python script.py input_file output_file
# If output_file is not specified, it simply
# writes the result to console
# Lines between #---v and #---^ are part of
# the template and should not be edited.

#----------v
import sys
#----------^

def rec(curr, index):
    r = 0
    for ch in perms[index]:
        if index is not letters-1:
            if curr+ch in words[index]:
                r += rec(curr+ch, index+1)
        else:
            if curr+ch in words[-1]:
                r += 1
    return r

#----------v
output = None
if len(sys.argv) == 3:
    output = open(sys.argv[2], 'w')
input = open(sys.argv[1])
#----------^

nums = input.readline().split("\n")[0].split(" ")
letters = int(nums[0])
words = [[] for i in range(letters)]
cases = []
for i in range(int(nums[1])):
    words[letters-1].append(input.readline().split("\n")[0])
    for a in range(letters-1):
        words[a].append(words[letters-1][-1][:a+1])
for i in range(int(nums[2])):
    cases.append(input.readline().split("\n")[0])

#----------v
for n in range(len(cases)):
#----------^

    perms = [[] for i in range(letters)]
    count = 0
    opened = False
    for ch in cases[n]:
        if ch == '(':
            opened = True
        elif ch == ')':
            opened = False
            count += 1
        else:
            perms[count].append(ch)
            if not opened: count += 1
    result = str(rec("", 0))

#----------v
    print("Case #"+str(n+1)+": "+result)
    if len(sys.argv) == 3:
        output.write("Case #"+str(n+1)+": "+result+"\n")
#----------^










