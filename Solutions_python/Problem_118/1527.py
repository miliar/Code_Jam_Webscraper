def palindrome(num):
    return str(num) == str(num)[::-1]

f = open('test.txt', 'r')
fout = open("output.txt", "w")
case = 0

pal = []

for i in range(1,10**7):
	if palindrome(i*i) and palindrome(i):
		pal.append(i*i)

print pal
for line in f:
	if case == 0:
		case+=1
		continue
	line = line.split()
	a = int(line[0])
	b = int(line[1])
	j2 = [i for i in pal if i >= a and i <= b]
	fout.write("Case #" + str(case) + ": " + str(len(j2)) + "\n")
	case += 1
