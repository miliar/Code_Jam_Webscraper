#Magician
import string;



#main program

#read file
infile = open('A-small-attempt0.in','r');
outfile = open('output.out','w');

#read case
cases = int(infile.readline().rstrip());

j = 1;
while (j <= cases):
	#read row1
	row1 = int(infile.readline().rstrip());
	nums1 = [];
	i = 0;
	while (i < 4):
		row = infile.readline();
		i = i + 1;
		if (i == row1):
			nums1 = row.split();
	row2 = int(infile.readline().rstrip());

	nums2 = [];
	i = 0;
	while (i < 4):
		row = infile.readline();
		i = i + 1;
		if (i == row2):
			nums2 = row.split();


	i = 0;
	result = [];
	#compare two string
	while (len(result) < 2 and i < len(nums1)):
		if (nums2.count(nums1[i]) != 0):
			result.append(nums1[i]);
		i = i + 1;

	outfile.write("Case #" + str(j) + ": ");
	if (len(result) == 0):
		outfile.write("Volunteer cheated!\n");
	elif (len(result) == 1):
		outfile.write(str(result[0]) + '\n');
	else:
		outfile.write("Bad magician!\n");

	j = j + 1;