import string

rot_map = {}
def isInMap(value):
    string_rep = str(value)
    for i in range(len(string_rep)):
        if string_rep in rot_map:
            return string_rep
        else:
            string_rep = ''.join((string_rep[-1], string_rep[:-1]))
    return False
def addToMap(value):
    string_in_map = isInMap(value)
    if string_in_map:
        rot_map[string_in_map] += 1
    else:
        string_in_map = str(value)
        rot_map[string_in_map] = 0
    return rot_map[string_in_map]

# parse input
f = open("input.txt", 'r')
num_lines = int(f.readline().strip())
lines = []
for line in f:
    total_pairs = 0
    borders = line.strip().split(' ')
    for i in range(int(borders[0]), int(borders[1])+1):
        total_pairs += addToMap(i)
    lines.append(total_pairs)
    rot_map = {}
f.close()

# write output
f = open("output.txt", 'w')
for i in range(num_lines):
    f.write( "Case #" + str(int(i+1)) +\
            ": " + str(lines[i]))
    if i != num_lines-1:
        f.write('\n')
f.close()
