import string, sys

input = file(sys.argv[1]).readline

output = open('out.txt', 'w')

for case in range(int(input())):
    total = 0
    friends = 0
    line = input()
    for level in range(int(line[0])+1):
		if total+friends<level:
			friends = level-total
		total = total + int(line[level+2])
    output.write("Case #" + str(case+1) + ": " + str(friends) + "\n")