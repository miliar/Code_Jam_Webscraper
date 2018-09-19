import math

def calc_num(string, index, curchar):
	count = 0
	newstr = string[index:]
	#print string, index, curchar, newstr
	if len(newstr) == 0:
		return 0
	elif len(newstr) == 1:
		if newstr == curchar:
			count +=1
		return count
	for char in newstr:
		if char == curchar:
			count +=1
		else:
			return count
	return count
	

def start():
	f = open("/home/jb/Downloads/input.txt", "r")
	f2 = open("/home/jb/Downloads/output.txt", "w")

	casecount = int(f.readline())

	for case in range(0, casecount):
		f2.write("Case #" + str(case + 1) + ": ")
		strings = []
		numstrings = int(f.readline())
		for curstrindex in range(0, numstrings):
			strings.append(f.readline())
		
		string1 = strings[0][:-1]
		string2 = strings[1][:-1]
		moves = 0

		copy1 = string1[:]
		copy2 = string2[:]
		
		currentchar = ''
		s1num = 0
		s2index = 0
		broken = False
		for char in copy1[:]:
			if char == currentchar or currentchar == '':
				s1num += 1
				currentchar = char
			else:
				#print char, currentchar
				s2num = calc_num(string2, s2index, currentchar)
				if s2num == 0:
					broken = True
					break
				s2index += s2num
				moves += abs(s1num - s2num)
				s1num = 1
				currentchar = char

		s2num = calc_num(string2, s2index, currentchar)

		if s2num == 0:
			broken = True
		else:
			moves += abs(s1num - s2num)
		if s2num + s2index != len(string2) and not broken:
			broken = True
		
		if broken:
			f2.write(str("Fegla Won") +"\n")
		else:
			f2.write(str(moves) +"\n")


if __name__ == '__main__':
	start()
