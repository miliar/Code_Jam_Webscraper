
def flip(c):
	if c == '+':
		return '-';
	else:
		return '+';

def check(panstr, k):
	c = 0;	
	for i in range(len(panstr)):
		if panstr[i] == '-':
			if i+k > len(panstr):
				return -1;
			else:
				c += 1;
			for j in range(i, i+k):
				panstr[j] = flip(panstr[j]);
	return c;

	

T = int(raw_input());
for i in range(T):
	S = raw_input().split(" ");
	K = int(S[1]);
	panstr = list(S[0]);

	ans = check(panstr, K);
	if ans == -1:
		print "Case #%d: IMPOSSIBLE" %(i + 1);
	else:
		print "Case #%d: %d" % (i+1, ans);

