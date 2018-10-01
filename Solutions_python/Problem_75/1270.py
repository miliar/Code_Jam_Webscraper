def ParseFile(path):
	inputFile = file(path, "r");
	nLines = inputFile.readline();
	commands = inputFile.readlines();
	inputFile.close();
	newPath=path[:path.find(".")+1]+"out";
	outputFile=file(newPath,"w");
	
	# read opposing 
	
	# analyze invokations
	k=1;
	for command in commands:
		parts=command.split();
		# read combinations
		comboDict={};
		nCombos=int(parts[0]);
		for i in range(1,nCombos+1):
			combo=parts[i];
			comboDict[combo[:2]]=combo[2];
			comboDict[combo[1::-1]]=combo[2];
		print(comboDict);
		
		oposList={};
		nOpos=int(parts[nCombos+1]);
		print(oposList)
		oposList=parts[nCombos+2:nCombos+2+nOpos];
		
		invokation=parts[nCombos+3+nOpos];
		result=[];
		cleared=False;
		
		for i in range(len(invokation)):
			if len(result)==0:
				result.append(invokation[i]);
			else:
				lastTwo=result[len(result)-1]+invokation[i];
				print(lastTwo)
				if lastTwo in comboDict:
					result[len(result)-1]=comboDict[lastTwo];
				else:
					for opos in oposList:
						if opos[0]==invokation[i] or opos[1]==invokation[i]:
							if opos[0]==invokation[i]:
								if opos[1] in result:
									result=[];
									cleared=True;
									break;
							else:
								if opos[0] in result:
									result=[];
									cleared=True;
									break;
					if cleared==False:
						result.append(invokation[i]);
					else:
						cleared=False;
		outString="Case #"+str(k)+": "+str(result)+"\n";
		outputFile.write(outString.replace('\'',''));
		k+=1;
	outputFile.close();
