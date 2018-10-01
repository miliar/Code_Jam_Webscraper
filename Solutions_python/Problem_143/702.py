def main():
	inp = open('input.txt')
	output = open('output.txt', 'w')
	cases = inp.readline().replace("\n", "")

	for n in range(0, int(cases)):
		case = inp.readline().replace("\n", "")
		print(case);
		listI = case.split()	
		res = int(listI[0]) & int(listI[1])
		print(res)
		'{0:08b}'.format(6)
		count = 0
		K = int(listI[2])
		for A in range(0, int(listI[0])):
			for B in range(0, int(listI[1])):
				if A & B < K:
					count+=1

		output.write("Case #"+str(n+1)+": "+str(count)+"\n")


	inp.close()
	output.close()





main()