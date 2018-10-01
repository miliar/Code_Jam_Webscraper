import sys,pdb,traceback

def one(arg):
	inputFileName="A-large.in"
	#inputFileName="oneSmall.in"
	try:
		
		with open(inputFileName,"r") as inputFile:
			totLines=int(inputFile.readline())
			iterator=0
			#pdb.set_trace()
			with open("one-l.out","w") as outputFile:
				while iterator < totLines:
					currLine=(inputFile.readline().splitlines()[0]).split(" ")
					maxShyness=int(currLine[0])
					shynessMap=currLine[1]
					tsc=0  #totalShynessCovered
					frndsReq=0
			
					i=0
					while i<len(shynessMap):
						if tsc<i and int(shynessMap[i])!=0:
						
							while(tsc<i):
								tsc+=1	
								frndsReq+=1
						tsc+=int(shynessMap[i])
				
						i+=1
				
			
			
			
			
					outputFile.write("Case #"+str(iterator+1)+": "+str(frndsReq)+"\n")
					iterator+=1
	except Exception as exc:
                	traceback.print_exc()
                        print(exc.args)
if __name__ == "__main__":
   one(sys.argv)
