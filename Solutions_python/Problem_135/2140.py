import sys


def solve(fname,outf):
	f = open(fname,'r')
	fout = open(outf,'w')
	T = int(f.readline())
	
	for k in range(0,T):
		x = int(f.readline())
		visit = [0]*17
		for i in range(0,4):
			line = f.readline()
			tokens = line.split()
			tokens = [int(item) for item in tokens]
			if i==x-1:
				for item in tokens:
					visit[item]=1
			
		y = int(f.readline())
		found = False
		fine = True
		key = -1
		for i in range(0,4):
			line = f.readline()
			tokens = line.split()
			tokens=[int(x)for x in tokens]
			if i==y-1:
				for item in tokens:
					if visit[item]==1 and found==False:
						found= True
						key = item
					else:
						if visit[item]==1 and found==True:
							fine = False

		fout.write("Case #%d: "%(k+1))
		if found and fine:
			fout.write("%d\n"%key)
		elif not found:
			fout.write("Volunteer cheated!\n")
		else:
			fout.write("Bad magician!\n")
				
		
	f.close()
	fout.close()	
if __name__=="__main__":
	fin = sys.argv[1]
	fout = sys.argv[2]
	solve(fin,fout)
