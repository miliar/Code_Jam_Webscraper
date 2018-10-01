import re
		
def main():
	f = open('input.in','r')
	fout = open('output.out','w')
	lines = f.readlines()
	L=int(lines[0].split(' ')[0])
	D=int(lines[0].split(' ')[1])
	N=int(lines[0].split(' ')[2])
	
	dic = []
	
	for word in lines[1:D+1]:
		dic.append(word.strip('\n'))
	
	case = 1
	
	for pattern in lines[D+1:]:
		print pattern
		
		out = ""
		p = pattern.strip('\n')
		inside = False
		for i in range(0,len(p)):
			if p[i]=='(':
				out+= '('
				inside = True
			elif p[i]==')':
				inside = False
				out = out.rstrip('|')
				out +=')'
			else:
				out += p[i]
				if inside:
					out += '|'
		out = out.rstrip('|')
		
		print out
		i=0
		p=re.compile(out)
		for word in dic:
			if p.match(word)!=None:
				i+=1
		
		
		output = "Case #%i: " % case
		output += str(i)
		output += '\n'
		case+=1
		
		fout.writelines(output)
		print output
		
	fout.close()
	
if __name__ == '__main__':
	main()