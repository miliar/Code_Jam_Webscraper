import datetime

calculator = {("1","1"):"1",
("1","i"):"i",
("1","j"):"j",
("1","k"):"k",
("-1","1"):"-1",
("-1","i"):"-i",
("-1","j"):"-j",
("-1","k"):"-k",
("i","1"):"i",
("i","i"):"-1",
("i","j"):"k",
("i","k"):"-j",
("-i","1"):"-i",
("-i","i"):"1",
("-i","j"):"-k",
("-i","k"):"j",
("j","1"):"j",
("j","i"):"-k",
("j","j"):"-1",
("j","k"):"i",
("-j","1"):"-j",
("-j","i"):"k",
("-j","j"):"1",
("-j","k"):"-i",
("k","1"):"k",
("k","i"):"j",
("k","j"):"-i",
("k","k"):"-1",
("-k","1"):"-k",
("-k","i"):"-j",
("-k","j"):"i",
("-k","k"):"1"
}

def solve():
    problemList = parseInput()
    problemCount = 1
    f = open("output.txt","w")
    for problem in problemList:
        print ("Start time problem " + str(problemCount) + ": " + datetime.datetime.now().isoformat())
        output = doProblem(problem)
        print ("End time problem " + str(problemCount) + ":" + datetime.datetime.now().isoformat())
        # put this into a file?
        if output:
            f.write("Case #"+str(problemCount)+": YES\n")
        else:
            f.write("Case #"+str(problemCount)+": NO\n")
        problemCount = problemCount + 1

        
def readInput():
    
    return f.read()
    
def parseInput():
    f = open("input.txt")
    numProblems = int(f.readline())
    problems = []
    for i in range(0,numProblems):
        problems.append([f.readline(), f.readline()])
    return problems
    
def doProblem(input):
    firstInput = input[0].strip()
    lengthOfString = int(firstInput.split(" ")[0])
    repeatStringTimes = int(firstInput.split(" ")[1])
    problemString = input[1].strip()
    currentValue = "1"
    valuesToFind = ["i","j","k","DONE - WOW THIS IS GROSS"]
    valuesToFind.reverse()
    nextValueLookingFor = valuesToFind.pop()
    for iteration in range(0,repeatStringTimes):
        for char in problemString:
            #start = ""+currentValue+"*"+char
            currentValue = calculator[(currentValue,char)]
            #print(""+start+"="+currentValue)
            if (len(valuesToFind)>0 and currentValue == nextValueLookingFor):
                nextValueLookingFor = valuesToFind.pop()
                currentValue = "1"
            

    return (len(valuesToFind)==0 and currentValue == "1")
    
    
solve()

