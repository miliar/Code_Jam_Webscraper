filer = open('B-small-attempt2.in','r')
output = open('B-small-attempt2.out','w+')
Ti = map(lambda x:int(x), filer.readlines())
T = Ti[0]

if(T >= 1 and T <= 100):
	for t in range(len(Ti)):
		if t > 0:
			num = Ti[t]
			if(num >= 1 and num <= 1000):
				if num < 10:
					output.write('Case #'+str(t)+': '+str(num)+'\r\n')

				elif num == int(''.join(sorted(list(str(num))))):
					output.write('Case #'+str(t)+': '+str(num)+'\r\n')
				else:
					for n in range(num,-1,-1):
						if n == int(''.join(sorted(list(str(n))))):
							output.write('Case #'+str(t)+': '+str(n)+'\r\n')		
							break;

			else:
				break;
output.close()
