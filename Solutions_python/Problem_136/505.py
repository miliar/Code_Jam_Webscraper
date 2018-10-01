import sys,os

def cookietime(C,F,X):
    # C = price for a cookie farm
    # F = rate of cookie production per farm
    # X = cookies needed to win
    cookies = 0
    rate = 2
    time = 0
    while cookies<X:
        tfarm = (C-cookies)/rate # time to save up for a cookiefarm
        tf =  tfarm + X/(rate+F) #time to build new farm and then reach X
        tx = (X-cookies)/rate #time to reach X cookies without building a new farm
        if tf < tx:
            time += tfarm
            rate += F
        else:
            time += tx
            cookies = X
        
    return time
    
def cookieclicker(infile,outfile):
    
    testcases = int(infile.readline())
    
    # for each testcase, read out the parameters X,F,C and calculate the time
    # then write the output line in outfile
    for t in range(testcases):
        [C,F,X] = [float(i) for i in infile.readline().replace('\n','').split(' ')]

        answer = cookietime(C,F,X)
        
        outfile.write('Case #'+str(t+1)+': '+str(answer)+'\n')
        

def main(argv):
    
    # read input file from command line arguments
    # pass input and output files to program
    if len(argv)!=1:
        print('Inputfile missing!')
    else:
        try:
            infile = open(argv[0],'r') 
            (fname,extension) = os.path.splitext(argv[0])
            outfile = open(fname+'.out','w')
            cookieclicker(infile,outfile)
            infile.close()
            outfile.close()
        except IOError as e:
            print(e)


if __name__ == "__main__":
  main(sys.argv[1:])