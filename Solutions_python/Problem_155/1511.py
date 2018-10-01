file1 = open("A-large.in", "r")
my_file = open("output.txt", "r+")


t = int(file1.readline())
i = 0
while (i < t):
	smax,shyness = file1.readline().split()
	totalstand = 0
	j = 0
	y = 0
	k = 0
	while (k< len(shyness)):
		if (totalstand >= k):
			totalstand += int(shyness[k])
		else:
			y += (k-totalstand)
			totalstand = k + int(shyness[k])
		k+=1	
	i+=1		
	my_file.write(("Case #%d: %d\n" % (i,y)))
my_file.close()
file1.close()
