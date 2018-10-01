import sys
import os


def main():
	file = sys.argv[1]
	outp = sys.argv[2]

	with open(outp, 'w') as w:
		with open(file,'r') as f:
			number = int(f.readline())
			for i in range(number):
				choose1 = int(f.readline())
				l1 = [f.readline() for j in range(4)]
				choose2 = int(f.readline())
				l2 = [f.readline() for j in range(4)]
				l1 = l1[choose1-1]
				l2 = l2[choose2-1]
				l1 = l1.strip()
				l2 = l2.strip()
				l1 = l1.split(" ")
				l2 = l2.split(" ")
				l1 = set(l1)
				l2 = set(l2)
				r = l1 & l2
				w.write("Case #"+str(i+1)+": ")
				if len(r)==1:
					w.write(list(r)[0])
				elif len(r)==0:
					w.write("Volunteer cheated!")
				else:
					w.write("Bad magician!")
				w.write("\n")
					
			

if __name__ == "__main__":
	main()
	
