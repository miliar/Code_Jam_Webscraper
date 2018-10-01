fin = open("B-small.in", 'r');
fout = open("B-small.out", 'w');

caseNum = int(fin.readline());

for case in range(caseNum):
    dataList = fin.readline().split();
    googlers = int(dataList[0]);
    surprise = int(dataList[1]);
    best = int(dataList[2]);
    great = 0;
    for g in range(3, 3 + googlers):
	score = int(dataList[g]);
        if score >= (best * 3 - 2):
            great += 1;
	elif (score > 2) and (score >= best * 3 - 4) and (surprise > 0):
            surprise -= 1;
	    great += 1;
    fout.write("Case #" + str(case+1) + ": " + str(great) +"\n");

fin.close();
fout.close();

	        

