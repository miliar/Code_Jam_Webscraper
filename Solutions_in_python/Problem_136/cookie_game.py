from __future__ import division

input_filename = "B-large.in"


def get_min_time(c, f, x):
	if f == 0.0:
		return str(round(x/2))
	curr_time, prev_time = c/2, 0
	n = 1 #Denotes the number of farms!
	while curr_time + x/(2 + n*f) <= prev_time + x/(2+ (n-1)*f):
		n += 1
		prev_time = curr_time
		curr_time += c/(2 + (n-1)*f)
	return str(round(prev_time + x/(2+ (n-1)*f), 7))
		

def main(t, fin, fout):
	preliminary_text = "Case #%s: %s \n"
	for i in xrange(t):
		line = fin.readline()
		c, f, x = map(float, line.split())
		result = get_min_time(c, f, x)
		fout.write(preliminary_text %(i+1, result))

if __name__ == "__main__":
	fin = open(input_filename, "r")
	fout = open("output_cookie_large.txt", "w")
	t = int(fin.readline().strip())
	main(t, fin, fout)
	fin.close()
	fout.close()