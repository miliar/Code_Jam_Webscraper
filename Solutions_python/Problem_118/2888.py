import fileinput
import math
import gmpy

def main(loc=""):
    raw = input('input location: ')
    f = open(raw,'r+')
    o = open("C:/Users/Matt/Desktop/output.txt",'w')
    num = int(f.readline()) #num of inputs
    board=""
    inp=[]
    for j in xrange(0,num):
        inp = readinput(f,1,0)
        inpstr = ''.join(inp)
        bounds = inpstr.split(" ")
        count = 0
        for i in xrange(int(bounds[0]),int(bounds[1])+1):
            if str(i) == str(i)[::-1]:
                if gmpy.is_square(i):
                    root=int(math.sqrt(i))
                    print root
                    if str(root) == str(root)[::-1]:
                        count += 1
        done(count,j,o)
        
    

def done(output,num,filename):
    result=""
    filename.write('Case #'+str(num+1)+': '+str(output)+'\n')
        

def readinput(filename,lines,trash=1): #read in filename x lines, trash y lines after
    inp=[]
    for i in xrange(0,lines):
        inp.append(filename.readline().replace('\n', ''))
    if trash !=0:
        for j in xrange(0,trash):
            filename.readline()
    return inp

main()
