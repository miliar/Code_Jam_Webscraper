def getInput(path):
        f = open(path)
        lines = f.readlines()
        f.close()
        return lines

def print_ouput():
	lines = getInput("./input.txt")
	no_cases = int(lines[0].strip())
	case = 1
	while (case<=no_cases):
		i=(case-1)*10 + 1
		answer1 = int(lines[i].strip())
		layout1 = [lines[i+1].split(),lines[i+2].split(),lines[i+3].split(),lines[i+4].split()]
		answer2 = int(lines[i+5].strip())
		layout2 = [lines[i+6].split(),lines[i+7].split(),lines[i+8].split(),lines[i+9].split()]
		sol = get_solution(layout1, layout2, answer1, answer2)
		print "Case #{0}: {1}".format(case,sol)
		case  += 1					
	

def get_solution(layout1, layout2, answer1, answer2):
	intersection = list(set(layout1[answer1-1]) & set(layout2[answer2-1]))
	length = len(intersection)
	if length == 0:
		return "Volunteer cheated!"
	elif length == 1:
		return intersection[0]
	else:
		return "Bad magician!"

print_ouput()
