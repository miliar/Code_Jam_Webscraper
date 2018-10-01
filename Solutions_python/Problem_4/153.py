def multiplicar(x,y):
    suma = 0
    for i in range(len(x)):
        suma = suma + (x[i]*y[i])
    return suma

def readInput(path_file_input, path_file_output):
    myFileIn = open(path_file_input, "r")
    myFileOut = open(path_file_output, "w")
    lines = myFileIn.readlines()
    myFileIn.close() 
    N = int((lines[0].split("\n"))[0])
    i = 1
    linea = 1
    while(i<N+1):
        S = int((lines[linea].split("\n"))[0])
        linea = linea +1
        x = []
        xcad = lines[linea].split("\n")[0]
#        print xcad
        xstr = xcad.split(" ")
#        print xstr
        for xiter in xstr:
            x.append(int(xiter))
#        print x
        linea = linea +1
        y = []
        ycad = lines[linea].split("\n")[0]
        ystr = ycad.split(" ")
        for yiter in ystr:
            y.append(int(yiter))
        x.sort()
        y.sort()
        y.reverse()
        xy = multiplicar(x,y)
        case = "Case #" + str(i) + ": " + str(xy) + "\n"
        myFileOut.write(case)
        linea = linea+1
        i = i + 1
    myFileOut.close()    

path_file_input = input("Input file path: (sample use 'x:/path/file.input'):  ")
path_file_output = input("Output file path: (sample use 'x:/path/file.output'):  ")
readInput(path_file_input, path_file_output)
print "OK"

            
        
        
