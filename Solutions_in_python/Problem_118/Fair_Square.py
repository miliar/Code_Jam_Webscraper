import Palindrone

fi = open('/media/gopal/ACADEMIC/PROJECTS/CODE_JAM/2013/ENTRY/FAIR_SQUARE/C-small-attempt0.in','r');
fout = open('/media/gopal/ACADEMIC/PROJECTS/CODE_JAM/2013/ENTRY/FAIR_SQUARE/C-small-attempt0_output.in','w');

case = 1
count = int(fi.readline());

for line in fi.readlines():
	
	s = line.split()	
	print s
	min = long(s[0])
	max = long(s[1])
	
	print " min ",min," max",max
	square=1
	i=1
	score=0
	p = Palindrone
	
	while(square<=max):
		square = i*i
		
		re = p.palindrome(i)
		if(re==1):		
			if( (square>=min) & (square<=max) ):
	#		 		print square
					result = p.palindrome(square)
					if(result==1):
						score=score+1
						print square
		i=i+1;

	print "no. of ",score

	str_result = "Case #%d: %d\n"%(case,score)
	
	print str_result
	fout.write(str_result)
	
	
	
	case = case+1
fi.close();
fout.close();
