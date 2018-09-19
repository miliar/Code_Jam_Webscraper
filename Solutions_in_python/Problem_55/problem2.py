import sys

fh = open("C-small-attempt0.in", "r")
fo = open("C-small-attempt0.out", "w")

line = fh.readline()
count = line.strip()

for num in xrange(int(count)):
    line = fh.readline()
    line = line.strip()
    (R, k, N) = line.split(" ")
    
    line = fh.readline()
    line = line.strip()
    groups = line.split(" ")
    
    next_grp = 0
    sum = 0
    for r in xrange(int(R)):
        once = 0
        for g in xrange(len(groups)):
            if (int(k) < (once + int(groups[next_grp]))):
                break
            else:
                once += int(groups[next_grp])
            if (next_grp == (len(groups)-1)):
                next_grp = 0
            else:
                next_grp += 1
                
        sum += once
    
    out = num + 1        
    fo.write("Case #" + str(out) + ": " + str(sum) + "\n")
         
    
fh.close()
fo.close()

if __name__ == '__main__':
    pass