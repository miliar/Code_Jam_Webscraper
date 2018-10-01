file = 'C-small'

nums = []
for i in range(0, 10**3+1):
    nums.append(i)

for pivot in range(2, 10**3+1):
    if nums[pivot] > 0:
        for j in range(2, 10**3):
            if j* pivot <= 10**3:
                nums[j*pivot] = 0
            else:
                break
print nums

thredholds = set()
for base in range(2, 10**3):
    if nums[base] > 0:
        prob = nums[base]
        for e in range(2, 10**3):
            if prob**e <= 10**3:
                thredholds.add(prob**e)
            else:
                break
thredholds.add(1)
print thredholds
    

def algorithm():
    pass

def process():
    n = int(fin.readline().rstrip())
    if n == 1: return '0'
    count = 0
    for x in thredholds:
        if n >= x:
            count += 1
    return str(count)

fin = open(file + '.in', 'r')
fout = open(file + '.out', 'w')

num_cases = int(fin.readline().rstrip())

for i in range(1, num_cases + 1):
    result = process()
    fout.write('Case #%d: %s\n' % (i, result))

fin.close()
fout.close()