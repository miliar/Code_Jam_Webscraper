C = 500.0;
F = 4.0;
X = 2000.0;

filename = "B-small-attempt1.in";
with open (filename, "r") as inputfile:
	with open ("answers.txt", "w") as outputfile: 

		data = inputfile.readlines();
		T = int(data[0]); # T test cases follow

		for i in range(len(data)):
			line = data[i];
			data[i] = line.replace('\n','');

		for ii in range(T):
			line = data[ii+1].split(' ')
			#print(line)

			C = float(line[0]) # C = 500.0 = init cookies you receive after 2 cookies per second
			F = float(line[1]) # F = 4.0 = cookies per second by farm
			X = float(line[2]) # X = 2000.0 = goal to get this number of cookies

			max_farms = 0;
			secondsList = [];
			initrate = 2; # start cookie rate at 2 cookies / second
			secondsList.append(X);
			secondsList.append(X / initrate);
			jj = 0;
			#print(secondsList[jj])
			#print(secondsList[jj+1])

			while (secondsList[jj] > secondsList[jj+1]): 
				# init
				cookies = 0;
				seconds = 0;
				secs_left = 0;
				farms = 0;
				while (farms <= max_farms):
					rate = initrate + F*farms # update cookie rate
					secs_elapsed = C / rate
					seconds = seconds + secs_elapsed
					farms = farms + 1; # update farm count
					secs_left = X / (rate + F) # secs left with one more farm
					#print(secs_elapsed)
				seconds = round(seconds + secs_left,7)
				max_farms = max_farms + 1
				jj = jj + 1;
				secondsList.append(seconds)

			string = "".join((": ",str(min(secondsList))));
			answer = "".join(("Case #",str(ii+1),string));
			print(answer)
			outputfile.write("".join((answer,'\n')))

readFile = open("answers.txt")
lines = readFile.readlines()
readFile.close()

w = open("answers.txt",'w')
w.writelines([item for item in lines[:-1]])
w.write(answer)
w.close()