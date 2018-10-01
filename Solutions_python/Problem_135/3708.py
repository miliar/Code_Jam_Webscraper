f=open("A-small-attempt0.in","r");
f1=open("output_file.txt","w")
lines=f.readlines();
no_tt=int(lines[0]);
tests=[]
for i in list(range(0,no_tt)) :
	tests.append({"row1":int(lines[1+i*10]),"row2":int(lines[6+i*10]),"cards1":lines[2+i*10:6+i*10],"cards2":lines[7+i*10:11+i*10]})
t=0
for i in tests:
	t=t+1
	matrix1=[]
	matrix2=[]
	for j in i["cards1"]:
		j=j.strip("\n");
		nums=j.split();
		matrix1.append(nums[:])
	for j in i["cards2"]:
		j=j.strip("\n");
		nums=j.split();
		matrix2.append(nums[:])
	count=0;
	num=99;
	for j in matrix1[i["row1"]-1]:
		if(j in matrix2[i["row2"]-1]):
			count=count+1
			num=j

	s="Case #"+str(t)+": "

	if(count==0):
		s=s+"Volunteer cheated!\n"
		f1.write(s);

	elif(count==1):
		s=s+str(num)+"\n"
		f1.write(s);

	else:
		s=s+"Bad magician!\n"
		f1.write(s);
