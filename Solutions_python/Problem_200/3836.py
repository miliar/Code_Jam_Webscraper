

# Import the file as a list of lines:

def sortString(sstr):
	flag=0
	for j in range(1,len(sstr)):
		if flag==0:
			if int(sstr[j])<int(sstr[j-1]):
				flag=1
				sstr[j-1]=str(int(sstr[j-1])-1)
		if flag==1:
			sstr[j]='9'

	

	tempInt=''.join(sstr);
	tempInt=int(tempInt);
	sstr=str(tempInt)
	sstr=list(sstr)
	
	if flag==0:
		return sstr

	else:
		return sortString(sstr)


file_in = 'in.txt'
file_out = 'out.txt'

with open(file_in,'rb') as fin, open(file_out,'wb') as fout:
	
	lines = fin.read().splitlines()
	case = 1
	cases=int(lines[0])
	lines=lines[1:]

	for i in range(cases):
		case = i+1
		output = sortString(list(lines[i]))

		
		output = 'Case #%d: %s\n' % (case,''.join(output))
		fout.write(output)
		
		

	# print (lines)

		







