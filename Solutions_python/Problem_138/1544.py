#!/usr/bin/python 

import sys
import fileinput

def main(argv):
	T = int(sys.stdin.readline())
	for count in range(1, T+1):
		# init variables
		score = 0
		dscore = 0

		N = int(sys.stdin.readline())
		
		# get naomi's blocks
		line = sys.stdin.readline()
		naomi = sorted(map(float, line.split()))
		
		#get ken's blocks
		line = sys.stdin.readline()
		ken = sorted(map(float, line.split()))

		# Normal war
		nn = list(naomi)
		kk = list(ken)
		while (len(nn) > 0):
			x = nn.pop(-1)
			for i in range(0, len(kk)):
				if kk[i] > x:
					del kk[i]
					break
				elif i == len(kk) - 1:
					kk.pop(0)
					score = score + 1

		# Deceitful war
		while (N > 0):
			if naomi[0] > ken[0]:
				#print "del", naomi[0], ken[0]
				del naomi[0]
				del ken[0]
				dscore = dscore + 1
			else:
				#print "del", naomi[0], ken[0], "<=="
				del naomi[0]
				del ken[-1]
			# for i in range(0, len(naomi)):
			# 	if naomi[i] > ken[-1]:
			# 		print "del", naomi[i], ken[0]
			# 		del naomi[i]
			# 		del ken[0]
			# 		dscore = dscore + 1
			# 		break
			# 	elif i == len(naomi) - 1:
			# 		print "del", naomi[0], ken[-1], " <=="
			# 		del naomi[0]
			# 		del ken[-1]
			N = N - 1

		dscore = dscore + len(ken)

		# print results
		ss = "Case #"+ str(count) + ": " + str(dscore) + " " + str(score)
		print(ss)

	pass

if __name__ == '__main__':
	main(sys.argv)



# int main (int argc, char *argv[]) {
	
# 	size_t T, count = 1;
# 	string line;
	
# 	// get T
# 	getline(cin, line);
# 	stringstream(line) >> T;

# 	// Helpful variables
# 	long double N;
# 	long int nscore, ndscore;

# 	// get all cases and process it
# 	for(size_t count = 1; count <= T; count++) {
# 		// get N
# 		getline(cin, line);
# 		stringstream(line) >> N;
		
# 		// read naomi's blocks
# 		getline(cin, line);
# 		istringstream ss(line);
# 		istream_iterator<string> begin(ss), end;
# 		vector<double> naomi(begin, end);

# 		// read ken's blocks
# 		//getline(cin, line);
# 		//ss(line);
# 		//begin(ss);
# 		//vector<double> ken(begin, end);


# 		// init case
# 		nscore = 0;
# 		ndscore = 0;
		
# 		// print output
# 		cout << "Case #" << count << ": " << ndscore << " " << nscore;
# 		cout << endl;
		
# 		//cout << "===========" << endl;
# 	}
	
# 	return 0;
# }