import time
starttime = time.time()

with open('D-small-attempt0.in', 'r') as f:
    data_raw = f.readlines()
f.closed

def solve(input):
    X, R, C = input
    if C > R:
        R, C = C, R
    if (R * C) % X > 0:
        return True
    if X > R:
        return True
    if X < 3:
        return False
    if X > 2 * C:
        return True
    if X == 3:
        return False
    if X == 4:
        if R == 2 or C == 2:
            return True
        return False
    return True #TODO X > 4
    
data_raw = data_raw[1:]
outputs = []
for line in data_raw:
    line = [int(x) for x in line.strip().split(' ')]
    outputs.append(solve(line))  

with open('D-small0.out', 'w') as f:
    i = 1
    outputstrings= []
    for output in outputs:
        if output:
            output = 'RICHARD'
        else:
            output = 'GABRIEL'
        outputstrings.append('Case #{0}: {1}'.format(i, output))
        i += 1
    f.write('\n'.join(outputstrings))
f.closed

print time.time() - starttime