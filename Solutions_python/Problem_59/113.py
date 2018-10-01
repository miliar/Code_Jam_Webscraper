#!/usr/bin/env python

import sys

def main():
	#f = file("test.in")
	f = file("A-large.in")
	fout= file("A-large.out", "w")
	T = int(f.readline())
	cnt = 1
	for i in range(T):
		cnt_mkdir = 0
		dirs = []
		creates = []
		N, M = map(int, f.readline().strip().split())
		for j in range(N):
			dirs.append(f.readline().strip())
		for j in range(M):
			creates.append(f.readline().strip())
		for d in creates:
			create_dirs = d[1:].split("/")
			for j in range(len(create_dirs)):
				current_dir = "/" + "/".join(create_dirs[:j+1])
				if current_dir in dirs:
					continue
				else:
					cnt_mkdir += 1
					dirs.append(current_dir)
		print >>fout, "Case #%d: %d" % (cnt, cnt_mkdir)
		cnt += 1

if __name__ == "__main__": main()
