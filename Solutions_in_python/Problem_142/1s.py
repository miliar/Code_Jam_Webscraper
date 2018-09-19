import sys

def removeDuplicate(L):
	if len(set(L)) == 1:
		return list(set(L))

	i = 0
	tmp = list()
	for i in xrange(len(L) - 1):
		if L[i] != L[i + 1]:
			tmp.append(L[i])

	if tmp[-1] != L[-1]:
		tmp.append(L[-1])
	return tmp

def isFelgaWin(A, B):
	tmp_A = removeDuplicate(A)
	tmp_B = removeDuplicate(B)


	if len(tmp_A) != len(tmp_B):
		return True
	for i in xrange(len(tmp_A)):
		if tmp_A[i] != tmp_B[i]:
			return True

	return False

def sol(A, B):
	A = list(A)
	B = list(B)
	if A == B:
		return 0
	if isFelgaWin(A, B):
		return "Fegla Won"
	counter = 0
	i = 0
	while A != B:
		if len(A) == i:
			A.append(B[i])
			counter += 1
			i += 1
			continue
		if len(B) == i:
			B.append(A[i])
			counter += 1
			i += 1
			continue
		if A[i] == B[i]:
			i += 1
			continue
		if A[i] == A[i - 1] and A[i] != B[i]:
			B.insert(i, A[i])
			counter += 1
		elif B[i] == B[i - 1] and A[i] != B[i]:
			A.insert(i, B[i])
			counter += 1
		i += 1

	return counter



fin  = open("A-small-attempt1.in", "r")
fout = open("output_1s.txt", "w")

case = int(fin.readline().strip())
for c in xrange(case):
	N = int(fin.readline().strip())
	a = fin.readline().strip()
	b = fin.readline().strip()
	print c

	fout.write("Case #" + str(c + 1) + ": " + str(sol(a, b)) + "\n")

fin.close()
fout.close()