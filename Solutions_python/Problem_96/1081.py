'''
Created on May 6, 2011

@author: jirasak
'''

def solve(i, num, surp, maxNum, rest):
    possible = maxNum * 3
    out = 0
    count = surp
    for e in sorted(rest)[::-1]:
        if e <= 3:
            if e == 0 and maxNum <= 0:
                out += 1
            elif e == 1 and maxNum <= 1:
                out += 1
            elif e == 2 and maxNum <= 1:
                out += 1
            elif e == 2 and (maxNum <= 2 and count > 0):
                out += 1
                count -= 1
            elif e == 3 and maxNum <= 1:
                out += 1
            elif e == 3 and (maxNum <= 2 and count > 0):
                out += 1
                count -= 1
        elif e >= possible - 2:
            out += 1
        elif e >= possible - 4 and count > 0:
            out += 1
            count -= 1
    return out

if __name__ == '__main__':
    fIn = file('B-large.in')
    inLines = fIn.readlines()
    fIn.close()
    
    inLines = inLines[1:]
    numLines = len(inLines)
    i = 0
    while i < numLines:
        line = inLines[i].strip()
        i += 1
        nums = line.split(' ')
        num = int(nums[0])
        surp = int(nums[1])
        maxNum = int(nums[2])
        rest = [int(x) for x in nums[3:]]
        data = solve(i, num, surp, maxNum, rest)
        print 'Case #%s: %s' % (i, data)
    