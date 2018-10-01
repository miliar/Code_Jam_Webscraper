"""
Code Jam 2011 Qualification Round
GoroSort by Warren Usui
"""
def GoroSort(fileHead):
    rootd = 'C:\\wutemp\\CodeJam\\2011'
    infile = "{0}\\{1}.in".format(rootd,fileHead)
    outfile = "{0}\\{1}.out".format(rootd,fileHead)
    fin = open(infile,'r')
    fout = open(outfile,'w')
    number = int(fin.readline())
    for iterv in xrange(0,number):
        fin.readline()
        txtin = fin.readline()
        charnums = txtin.split(" ")
        vind = 1
        cntr = 0
        for numba in charnums:
            nval = int(numba)
            if not nval == vind:
                cntr += 1
            vind += 1
        odata = "Case #{0}: {1}.000000\n".format(iterv+1, cntr)
        fout.write(odata)
        
if __name__ == '__main__':
    GoroSort('D-large')
    
