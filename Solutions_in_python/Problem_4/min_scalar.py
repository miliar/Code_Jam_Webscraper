#!/lsi/soft/CFR/bin/python
import sys
readfile = sys.argv[1]
writefile = readfile + ".out"

open_read_file = open(readfile,'r')
open_write_file = open(writefile,'w')
num_cases = int(open_read_file.readline())
#case = 0
#for line in open_read_file.readlines():
# if firstline == 0:
#    firstline = 1
#    num_cases = int(line)
# else:
#    case = case + 1

for case in range(num_cases):
    width = int(open_read_file.readline())
    vec1 = open_read_file.readline().split()
    vec2 = open_read_file.readline().split()
    for index in range(width):
        vec1[index] = int(vec1[index])
        vec2[index] = int(vec2[index])
        
    
    print vec1
    print vec2
    vec1.sort()
    vec2.sort()
    vec2.reverse()
    print vec1
    print vec2
    total = 0
    for index in range(width):
        total = total + vec1[index]*vec2[index]
    print total
    open_write_file.write("Case #")
    open_write_file.write(str(case+1))
    open_write_file.write(": ")
    open_write_file.write(str(total))
    open_write_file.write('\n')
