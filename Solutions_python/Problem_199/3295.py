def toggle(s,i,k):
	if len(s)< i+k :
		return s
	for j in range(k):
		if s[j+i] == '+':
			s[j+i] = '-'
		else:
			s[j+i] = '+'
 	return s
def check(s):
	for i in range(len(s)):
		if s[i] != '+':
			return False
	return True

def main():
	filename = "in.txt"
	data =  open(filename,'r').read().strip().split('\n')[1:]
	p = 0
	for row in data:
		p+=1
		row = row.split()
		s = list(row[0])
		k = int(row[1])
		count = 0
		for i in range(len(s)):
			if s[i]=='-':
				count+=1
				s = toggle(s,i,k)
		if(check(s)):
			print ''.join(['Case #',str(p),': ',str(count)])
		else:
			print ''.join(['Case #',str(p),': IMPOSSIBLE'])

if __name__ == '__main__':
   main()
