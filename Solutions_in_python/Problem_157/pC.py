table = [
['1','i','j','k'],
['i','-1','k','-j'],
['j','-k','-1','i'],
['k','j','-i','-1']
]

key = ['1', 'i', 'j', 'k']

def multiply(c1, c2):
	s = ""
	if len(c1) - len(c2):
		s = "-"
	s += table[key.index(c1[-1])][key.index(c2[-1])]
	if len(s) == 3:
		return s[2]
	elif len(s) == 2 or len(s) == 1:
		return s
	else:
		# print("UHOH")
		return "0"

def evaluate(string):
	# print(string)
	arr = list(string)
	for x in range(1, len(string)):
		arr[0] = multiply(arr[0], arr[x])
	return arr[0]

def sameletter(string):
	for x in range(1, len(string)):
		if string[x-1] != string[x]:
			return False
	return True

def isIJK(info, unit):
	L = int(info.split()[0])
	N = int(info.split()[1])
	string = unit * N

	if sameletter(unit) or len(string) < 3:
		return 'NO'
	if len(string) == 3:
		if string == 'ijk':
			return 'YES'
		else:
			return 'NO'
	curI = string[0]
	for i in range(1, len(string) - 1):
		if curI == 'i':
			for j in range(i+1, len(string)):
				if evaluate(string[i:j]) == 'j':
					if evaluate(string[j:]) == 'k':
						return 'YES'# = ' + string[:i] + " | " + string[i:j] + " | " + string[j:]
					# return 'YES'
		curI = multiply(curI, string[i])
	return 'NO'


def isIJKShort(info, unit):
	L = int(info.split()[0])
	N = int(info.split()[1])
	string = unit * N
	if sameletter(unit) or len(string) < 3:
		return 'NO'
	if evaluate(string) == '-1':
		return 'YES'
	return 'NO'

def isIJKShort1(info, unit):
	L = int(info.split()[0])
	N = int(info.split()[1])
	string = unit * N
	if sameletter(unit) or len(string) < 3:
		return 'NO'
	if evaluate(string) == '-1':
		return isIJK(info, unit)
	return 'NO'


def main():
	print(evaluate('iiiijjjjjj'))
	file1 = open('C-small-attempt3.in','r')
	file2 = open('outfile.txt','w')
	caseNumber = int(file1.readline())
	cases = file1.read().split('\n')
	for x in range(0, caseNumber*2, 2):
		file2.write("Case #" + str((x+2)//2) + ": " + isIJKShort1(cases[x], cases[x+1]) + "\n")
main()