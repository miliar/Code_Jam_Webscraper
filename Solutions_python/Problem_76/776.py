#coding:utf-8
import sys

def do_one_case(fin):
	ans = ("")
	N = int(fin.readline().rstrip())
	C = map(int, fin.readline().split())
#	print N
#	print C
	ans = 0
	for i in C:
		ans = ans^i
	if ans == 0:
		return str(sum(C) - min(C))
	else:
		return "NO"


def main(fin,fout):
	N = int(fin.readline())
	for i in xrange(N):
		result = "Case #"+str(i+1)+": "+do_one_case(fin)
		print result
		fout.write(result+"\n")


if __name__ == "__main__":
	import sys
	if len(sys.argv) == 2:
		fin = open(sys.argv[1].upper() + "-small-attempt0.in")
	elif len(sys.argv) == 3:
		if sys.argv[1] == sys.argv[2]: #誤入力防止
			fin = open(sys.argv[1].upper() + "-large.in")
	else:
		fin = open("zinput.txt")
	fout = open("clarge.txt","w")
	main(fin,fout)
	fin.close()
	fin.close()
#	main(sys.stdin)

