import sys

sys.stdin = open("in.txt", 'r')
sys.stdout = open("out.txt", 'w')

num = input()


def check_correct(st):
	if st.find('-') == -1:
		return True
	return False


def flip(st, ind, k):
	st_new = ""
	for x in range(ind, ind+k):
		if st[x] == "+":
			st_new += "-"
		else:
			st_new += "+"
	#print(ind)
	#print(st[ind-1])
	#print(st_new)
	res_st = st_new + st[ind+k:]
	if ind != 0:
		res_st = st[:ind] + res_st
	return res_st


def make_correct(st, k):
	steps = 0
	while st.find('-') > -1:
		steps += 1
		ind = st.find('-')
		if len(st) - ind < k:
			return False
		st = flip(st, ind, k)
	return steps


#while not check_tidy(st):
#	st = make_tidy(st)

casenum = 1
for i in range(0, int(num)):
	st = input()
	steps = 0
	if not check_correct(st):
		steps = make_correct(st.split()[0], int(st.split()[1]))
		if steps == False:
			steps = "IMPOSSIBLE"
	steps = str(steps)
	print("Case #" + str(casenum) + ": " + steps)
	casenum += 1