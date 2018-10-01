# Tidy Numbers

def tidyNumbers(tc):

	for testcases in xrange(tc):

		last_number = input()

		for number in xrange(last_number, 0, -1):
			
			a = list(str(number))
			flag = 0

			for i in xrange(len(a)-1):

				if a[i] <= a[i+1]:
					flag += 1

			if flag == len(a)-1:
				answer = ''.join(a)
				break


		print "Case #{}: {}".format(testcases+1, answer)

tidyNumbers(input())