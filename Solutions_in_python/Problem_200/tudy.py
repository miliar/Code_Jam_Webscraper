cases = int(input())
for i in range(cases):
	num = int(input());
	digs = list(str(num))
	for j in range(len(digs)-1):
		if(int(digs[len(digs)-2-j]) > int(digs[len(digs)-1-j])):
				#print(digs[len(digs)-2-j],digs[len(digs)-1-j])
			new = str(int(digs[len(digs)-2-j])-1)
				#print(new)
			digs[len(digs)-2-j] = new
			temp = len(digs)-2-j+1
				#print(temp)
			while(temp < len(digs)):
				digs[temp] = '9'
				temp = temp + 1;
			if(digs[0] == '0'):
				del(digs[0])
				
	digs = int(''.join(digs));
	print("Case #"+str(i+1)+":",digs);
			
		
		
	