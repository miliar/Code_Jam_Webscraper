def main(debug):
	t= input()
	f=open('output.txt','w')
	for i in range(t):
		line=raw_input()
		r=int(line.split(' ')[0])
		c=int(line.split(' ')[1])
		grid=[['?' for j in range(c)] for k in range(r)]
		rowappear=[False for j in range(r)]
		for j in range(r):
			line=raw_input()
			line=list(line)
			for k in range(len(line)):
				grid[j][k]=line[k]
				if line[k]!='?':
					rowappear[j]=True
		fillAbove=False
		count=0
		cons=True
		lastI='?'
		for j in range(r):
			k=0
			fp=0
			if rowappear[j]==True:
				cons=False
				while(grid[j][fp]=='?'):
					fp+=1
				lastI=grid[j][fp]
				if fp>0:
					for k in range(fp):
						grid[j][k]=grid[j][fp]
				k=fp+1
				while k<c:
					if grid[j][k]=='?':
						grid[j][k]=lastI
					else:
						lastI=grid[j][k]
					k+=1
				if fillAbove==True:
					for m in range(count):
						k=0
						for k in range(c):
							grid[j-m-1][k]=grid[j][k]
					fillAbove=False
				if j<r-1:
					if rowappear[j+1]==False:
						k=0
						for k in range(c):
							grid[j+1][k]=grid[j][k]
						rowappear[j+1]=True
			if cons==True and rowappear[j]==False:
				if(fillAbove==False):
					fillAbove=True
					count=1
				else:
					count+=1
		if debug==True:
			print("Case #{}:".format(i+1))
			for j in range(r):
				print(''.join(grid[j]))
		else:
			f.write('Case #{}:\n'.format(i+1))
			for j in range(r):
				f.write(''.join(grid[j]))
				f.write('\n')
	f.close();


if __name__=='__main__':
	main(False)