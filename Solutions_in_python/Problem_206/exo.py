import sys
import solver

if __name__=="__main__":

    outf = sys.stdout
    try:
        filename = sys.argv[1]
        if len(sys.argv) == 3 and sys.argv[2] == "final":
            outputfilename = filename.replace('in','out')
            outf = open(outputfilename,'w')             
    except IndexError:
        print("Arguments needed.\n Use: python exo.py <Input>")
        sys.exit()
    inf = open(filename,'r')

    N = int(inf.readline())
    
    for case in range(N):
        solver.solve(inf,outf,case+1)
