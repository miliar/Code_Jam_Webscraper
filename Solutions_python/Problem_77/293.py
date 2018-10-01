import sys

def solve(nums):
    end = sorted(nums)
    
    counter = 0
    for idx in range(0, len(nums)):
        if (nums[idx] == end[idx]):
            counter += 1
            
    return float(len(nums)) - float(counter)

f = open(sys.argv[1], "r")
output = open(sys.argv[1] + ".results", "w+")

f.readline() # kill the first line, no. of test cases
lines = f.readlines()

case_id = 1
for idx in range(0, len(lines) / 2):
    nums = map(lambda x: int(x), lines[2 * idx + 1].split(' '))
    val = solve(nums)
    
    print val    
    
    output.write("Case #%d: %f\n" % (case_id, val))
    case_id += 1

f.close()
output.close()
