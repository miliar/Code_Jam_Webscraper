import sys

TIDY = {1 : ["1","2","3","4","5","6","7","8","9"],
		2 : ['11', '12', '13', '14', '15', '16', '17', '18', '19', '22', '23', '24', '25', '26', '27', '28', '29', '33', '34', '35', '36', '37', '38', '39', '44', '45', '46', '47', '48', '49', '55', '56', '57', '58', '59', '66', '67', '68', '69', '77', '78', '79', '88', '89', '99']}

def melt(n):
	if n-1 not in TIDY:
		melt(n-1)
	
	#print "Melting %d... " % n,
	
	TIDY[n] = []
	for i in range(len(TIDY[n-1])):
		for j in range((int(TIDY[n-1][i]) % 10) - 1, len(TIDY[1])):
			num = "".join([TIDY[n-1][i],TIDY[1][j]])
			TIDY[n].append(num)
			
	#print "Done!"

def generate(length=2):
	if length in TIDY:
		return
	
	# not generated - even
	if length % 2 == 0:
		melt(length / 2, length / 2)
	else:
		melt(1, length-1)
		

def last_tiny_till_n(n):
	index = len(str(n))
	try:
		joint = TIDY[index] + TIDY[index-1]
	except:
		joint = TIDY[1]
	for i in range(len(joint)):
		if int(joint[i]) == n:
			return joint[i]
		elif int(joint[i]) > n:
			return joint[i-1]
		

def run_case(case_params):
	case_params = case_params.strip()
	n = int(case_params)
	return last_tiny_till_n(n)
	
def main():
	input = open(sys.argv[1], 'rb').readlines()
	number_of_cases = int(input[0])
	cases = input[1:number_of_cases+1]
	
	melt(19)
	
	for i, case in enumerate(cases):
		ans = run_case(case)
		print "Case #%d: %s" % (i+1, ans)
		
if __name__ == "__main__":
	main()


	