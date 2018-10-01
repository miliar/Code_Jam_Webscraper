import sys

class RepeatString:
    def __init__(self, s):
        self.letters = []
        self.freq = []
        current_letter = s[0]
        current_freq = 1
        for c in s[1:]:
            if c == current_letter:
                current_freq += 1
            else:
                self.letters.append(current_letter)
                self.freq.append(current_freq)
                current_letter = c
                current_freq = 1
        self.letters.append(current_letter)
        self.freq.append(current_freq)
                

    def match(self, repeat):
        if not (len(self.letters) == len(repeat.letters)):
            return False
        for i in range(len(self.letters)):
            if not (self.letters[i] == repeat.letters[i]):
                return False
        return True

def average(nums, i):
    if len(nums) == 0:
        return 0
    total = 0.0
    for n in nums:
        total += n[i]
    return total / len(nums)

def closest(nums, num, i):
    min_distance = abs(nums[0][i] - num)
    cl = nums[0][i]
    for n in nums:
        if abs(n[i] - num) < min_distance:
            min_distance = abs(n[i] - num)
            cl = n[i]
    return cl

def distance(nums, num, i):
    d = 0
    for n in nums:
        d += abs(n[i]  - num)
    return d

# Set up the input and output files
f = sys.argv[1]
sys.stdin = open(f, 'r')
sys.stdout = open(f[:-2] + "out", 'w')

# Read in T
total_cases = int(input())
fegla = "Fegla won"
result = "Win possible"
for case_number in range(1, total_cases + 1):
    result = "Possible"
    # Read in C and W
    num_strings = int(input())
    pattern = None
    freqs = []
    for i in range(num_strings):
        s = RepeatString(input())
        if pattern is not None:
            if not s.match(pattern):
                result = fegla
                break
        else:
            pattern = s
        freqs.append(s.freq)
    if result != fegla:
        result = 0
        for i in range(len(freqs[0])):
            goal = closest(freqs, average(freqs, i), i)
            result += distance(freqs, goal, i)
    print('Case #{0}: {1}'.format(case_number, result))


