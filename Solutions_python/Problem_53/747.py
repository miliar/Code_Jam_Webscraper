
fread=open('C:\Users\Sandip\Desktop\A-large.in','r')
fwrite=open('C:\Users\Sandip\Desktop\FINAL1.out','w')


total_cases=fread.readline().strip()
for i in range(int(total_cases)):
	line = fread.readline().strip()
	n= int(line.split()[0] )# n = number of snappers 10
	k = int ( line.split()[1] ) # k = number of times snaps 100
	val=pow(2,n)-1
	
	if k < val:
		o_string="Case #"+str(i+1)+": OFF\n"
	elif k==val:
		o_string="Case #"+str(i+1)+": ON\n"
	elif k%( val +1 )==val  :
		o_string="Case #"+str(i+1)+": ON\n"
	else:
		o_string="Case #"+str(i+1)+": OFF\n"
	fwrite.write(o_string)
    





fread.close()
fwrite.close()


