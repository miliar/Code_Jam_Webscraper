import os, sys

os.chdir('C:\Users\Morgan\My Dropbox\programming\gcj')

def read_input(filename):
    with open(filename, 'r') as f:
        read_data = f.read()
#    print read_data
    lines = read_data.split('\n')
#    print lines
    return lines

def parse_lines(lines):
    test_case_count = int(lines[0])
    test_cases = []
    for line in lines[1:]:
        nums = [int(num) for num in line.split()]
        test_cases.append(tuple(nums))
#    print test_cases
    return (test_case_count, test_cases)

def calculate(test):
    test_case_count = test[0]
    tests = test[1]
    count = 0
    saveout = sys.stdout
    f = open('out.txt','w')
    sys.stdout = f
    for case in tests:
        count +=1
        if count <= test_case_count:
            max = (2**case[0])
            flips = case[1]
            print_case(count, max, flips)
    f.close()
    sys.stdout = saveout
    
def print_case(count, max, flips):
    state = "OFF"
    if flips == 0:
        print "Case #" + str(count) + ": " + state
    elif max == 1:
        if flips %2 == 0:
            print "Case #" + str(count) + ": " + state
        else:
            state = "ON"
            print "Case #" + str(count) + ": " + state
    else:
        if(flips%max == max-1):
            state = "ON"
        print "Case #" + str(count) + ": " + state
