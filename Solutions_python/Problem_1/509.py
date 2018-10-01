#!/usr/bin/python
if __name__ == '__main__':
	import sys, string
	infile = open('temp.txt', 'r');
	outfile = open('out.txt', 'w');

	lines = infile.readlines();

	infile.close();

        numTest = 0;
	i = 1;

	while ((i < len(lines)) & (numTest < int(lines[0]))):
		outfile.write("Case #" + str(numTest + 1) + ": ");

		numSwitch = 0;

		numServer = int(lines[i]);
		i = i + 1;

		serverList = lines[i:(i + numServer)];
		i = i + numServer;

                numSearch = int(lines[i]);
		i = i + 1;

		searchList = lines[i:(i + numSearch)];
		i = i + numSearch;

		#print(numServer);
		#print(serverList);
		#print(numSearch);
		#print(searchList);

		avaliableList = serverList[:];

		j = 0;
		while (j < len(searchList)):
			search = searchList[j];

			if (avaliableList.count(search) > 0):
				if (len(avaliableList) == 1):
					numSwitch = numSwitch + 1;
					avaliableList = serverList[:];
					#print(search);
					#print(serverList);
					#print(numSwitch);
					j = j - 1;

				else:
					avaliableList.remove(search);
			
			j = j + 1;
					
		#print(avaliableList[0]);
		#print(numSwitch);
		outfile.write(str(numSwitch) + "\n");
		numTest = numTest + 1;
		
		#try:
		#	input();
		#except:
		#	print("next");

	outfile.close();
	print("DONE");

	