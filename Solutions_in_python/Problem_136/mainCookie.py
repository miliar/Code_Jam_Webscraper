import FileIO
import sys

# Dat = FileIO.ReadFile("Files/A-small-practice.in", ' ','int', True)
# Dat = FileIO.ReadFile("Files/MagicTrickTest.txt", ' ','int', False)
# Dat = FileIO.ReadFile("Files/A-small-attempt0.in", ' ','int', False)
# Dat = FileIO.ReadFile("Files/MinesTest.txt", ' ','int', True)
# Dat = FileIO.ReadFile("Files/CookieGame.txt", ' ','float', True)
Dat = FileIO.ReadFile("Files/B-large.in", ' ','float', True)
numprobs = int(Dat[0][0])
print "Problems: " + str(numprobs)
del Dat[0]


print sys.getrecursionlimit()
sys.setrecursionlimit(10000000)
print sys.getrecursionlimit()
# raw_input(".")
Cases = []
def CookieMath(Cases,C,F,X,S,FN,T,TW):
	# print("Go")
	FN = FN +1
	TW = TW + C/S
	S = S + F
	TNEW = TW + X/S

	# print(TNEW,T)
	# raw_input("...")

	if TNEW <= T:
		# print("TNEW", T)
		T = TNEW
		Cases[len(Cases)-1] = TNEW
		CookieMath(Cases,C,F,X,S,FN,T,TW)
	else:
		# print T
		Cases[len(Cases)-1] = T
		return T
	
while len(Dat) > 0:
# if 1:
	# print("============")
	C = Dat[0][0]  #Farm Price
	S = 2.0        #Current Cooke Rate
	F = Dat[0][1]  #Cookies Per Second for each farm
	FN = 0
	X = Dat[0][2]  #Winning Condition
	del Dat[0]
	T = 0
	TW = 0
	# print(C,F,X)

	T = X/S
	Cases.append(0.000)
	CookieMath(Cases,C,F,X,S,FN,T,TW)
# print Cases

FileIO.WriteCaseFile("out.txt", Cases, True) 

# 	R = Dat[0][0]
# 	C = Dat[0][1]
# 	M = Dat[0][2]
# 	del Dat[0]


# 	# M = 21
# 	# print(R*C-4)
# 	# if R*C - 4 < M:
# 		# Cases.append(Impossible)
# 		# print Impossible
# 	# else:
# 	Mat = ['.']*R
# 	for i, val in enumerate(Mat):
# 		Mat[i] = ['.']*C
# 		# print Mat[i]
# 	Mat[0][0] = 'c'
# # for (x in range (0,M)):
# 	x = 0
# 	# while x < M:
# 	for i, vali in enumerate(Mat):
# 		for j, valj in enumerate(Mat[i]):
# 			if (len(Mat)-1 - i > 1 or len(Mat[i])-1-j > 1) and x < M:
# 				Mat[len(Mat)-1-i][len(Mat[i])-1-j] = '*'
# 				x = x + 1 
# 	for i, val in enumerate(Mat):
# 		print Mat[i]

# 	if x == M:	
# 		Cases.append(Mat)
# 	else:
# 		Cases.append(Impossible)

# print ("====")
# # print Cases
# FileIO.WriteCaseFileMines("out.txt", Cases, True) 


	# for i, val in enumerate(Mat):
	# for i, val in enumerate(Mat):
# BadMagic = "Bad magician!"
# Cheater  = "Volunteer cheated!"


# Cases = []
# while len(Dat) > 0:
# # if 1:
# 	print("---")
# 	Mat1 = []
# 	Mat2 = []
# 	A1 = Dat[0][0]
# 	del Dat[0]
# 	Mat1.append(Dat[0])
# 	del Dat[0]
# 	Mat1.append(Dat[0])
# 	del Dat[0]
# 	Mat1.append(Dat[0])
# 	del Dat[0]
# 	Mat1.append(Dat[0])
# 	del Dat[0]

# 	A2 = Dat[0][0]
# 	del Dat[0]
# 	Mat2.append(Dat[0])
# 	del Dat[0]
# 	Mat2.append(Dat[0])
# 	del Dat[0]
# 	Mat2.append(Dat[0])
# 	del Dat[0]
# 	Mat2.append(Dat[0])
# 	del Dat[0]

# 	# print(A1)	
# 	# print(Mat1)
# 	# print(A2)
# 	# print(Mat2)


# 	# for i, val in enumerate(Mat1[A1]):
# 	# 	print("Hi")

# 	# print(Mat1[A1])
# 	Nums = []
# 	for i, val in enumerate(Mat2[A2-1]):
# 		# print val
# 		if val in Mat1[A1-1]:
# 			print (val)
# 			Nums.append(val)
# 			# Nums = []
# 	# for i, val in enumerate(Nums):
# 	if len(Nums) == 0:
# 		# Nums[i] =[]
# 		# Nums[i] = Cheater
# 		Cases.append(Cheater)
# 	elif len(Nums) > 1:
# 		# Nums[i] = []
# 		# Nums[i] = BadMagic
# 		Cases.append(BadMagic)
# 	else:
# 		Cases.append(Nums[0])

# # print Cases
# 	# l1.sort()
# 	# l2.sort(reverse = True)
# 	# l3 = []
# 	# for i, val in enumerate(l1):
# 	# 	l3.append(l1[i] * l2[i])
# 	# Cases.append(sum(l3))

# FileIO.WriteCaseFile("out.txt", Cases, True) 
