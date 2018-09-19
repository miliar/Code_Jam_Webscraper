def getCase(archive):
    '''It requires cursor set at the start of the input file'''
    line=archive.readline()
    case = line.split()
    return case

def startExercise():
    '''Open the input file'''
    archive = open("input")
    cases = archive.readline()
    return archive,cases

def openOutput():
    archive = open("output","w")
    return archive

def writeCase(n,archive,output):
    archive.write("Case #"+str(n+1)+": "+str(output)+'\n')
    print "Case #"+str(n+1)+": "+str(output)+'\n'

def finishExercise(input,output):
    input.close()
    output.close()
