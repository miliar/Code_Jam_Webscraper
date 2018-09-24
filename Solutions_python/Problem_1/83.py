#!/usr/local/bin/python

# Final answer obtained by
# ./scriptname.py -q -i A-small.in
# or
# ./scriptname.py -q -i A-large.in

#Python 2.5.2 (r252:60911, May  6 2008, 16:32:45) 
#[GCC 4.1.2 20070626 (Red Hat 4.1.2-14)] on linux2

#snippets from http://docs.python.org/lib/module-optparse.html

# 4:03 pm on Wed July 16

# Saving the universe



import sys
from optparse import OptionParser
import string


def usage():
    print sys.argv[0]," --from=dir --to=dir"

def process_args():
    parser = OptionParser()
    parser.add_option("-i", "--input", dest="fname",
                  help="Input file name.", metavar="DIR", default="A-small.in")
    parser.add_option("-q", "--quiet",
                  action="store_false", dest="verbose", default=True,
                  help="don't print status messages to stdout")
    (opts, args) = parser.parse_args()
    return opts,args

def process_next_case(filein,case=0):
    # Read the next line
    try:
        nextline=string.strip(filein.readline())
    except:
        return -1  
    if len(nextline)<=0:
        return -2

    #Process the line
    if opts.verbose:
        print nextline,len(nextline)
    vars=nextline.split(' ')
    if len(vars)<>3:
        return -3

    numin=vars[0]
    lang1=vars[1]
    lang2=vars[2]
    if opts.verbose:
        print numin,lang1,lang2
    
    value="0"
#    value=langtodecimal(numin,lang1)
#    value=decimaltolang(value,lang2)


    print "Case #"+str(case)+":  "+value

    return 1



def main():

    if opts.verbose:
        print "Input = "+opts.fname

    # Open the input file
    try:
        filein=open(opts.fname,"r")
    except:
        print "Failed to open "+fname        
    if opts.verbose:
        print opts.fname+" is open."

    # Read first line (the number of cases)
    try:
        numcases=int(string.strip(filein.readline()))
    except:
        print "Failed to read first line (number of cases)"
        return -1    
    if opts.verbose:
        print str(numcases)+" cases in file."

    # Check limit on num cases
    if numcases<=0 or numcases>20:
        print "   Too many cases in file. Exiting..."
        return -2
    
    # Loop over cases
    count=0
    while 1:
        count+=1
        #break after we have processed all cases
        if count>numcases:
            return 0
        if opts.verbose:
            print ""
            print "Case "+str(count)+"/"+str(numcases)
 
        # Read in the number of engines
        try:
            numengines=int(string.strip(filein.readline()))
        except:
            print "Failed to read number of engines"
            return -3
        if numengines==0:
            return 0
        # Read in the engine names
        enginelist=[]
        for i in range(numengines):
            nextengine=string.strip(filein.readline())
            enginelist.append(nextengine)
        
        if opts.verbose:
            print "   %d engines in case %d" % (numengines, count)
            print "   %d engines in case %d" % (len(enginelist),count)

        # Error if number of engines in list is not equal to numengines
        if len(enginelist)<>numengines:
            return -4

        # Read in the number of queries
        try:
            numquery=int(string.strip(filein.readline()))
        except:
            print "Failed to read number of queries"
            return -5
        if numquery==0:
            print "Case #%d: %d" % (count,0)
            continue
        # Read in the query list
        querylist=[]
        for i in range(numquery):
            nextquery=string.strip(filein.readline())
            querylist.append(nextquery)
        
        if opts.verbose:
            print "   %d queries in case %d" % (numquery, count)
            print "   %d queries in case %d" % (len(querylist),count)

        # Error if number of engines in list is not equal to numengines
        if len(querylist)<>numquery:
            return -6

        # Here I cheat in order to get last element of array correct
        querylist.append(querylist[len(querylist)-1])

        # Find answer
        searchlist=[]
        cmax=0
        lpos=0
        while 1:
            for test1 in enginelist:
                cpos=0
                nc=0
                for test2 in querylist:
                    nc+=1
                    if nc>len(querylist):
                        if opts.verbose:
                            print " break 1"
                        break
                    if nc<lpos:
                        continue
                    if opts.verbose:
                        print "      %d %s %s" % (nc, test1,test2)
                    if test2==test1:                        
                        if opts.verbose:
                            print " break 2"
                        break
                if opts.verbose:
                    print "   exit loop2 with nc=%d "%nc
                if nc>cmax:
                    cmax=nc
                    cbest=test1
                    ncbest=nc
            if opts.verbose:
                print "   exit loop1 with ncbest=%d "%ncbest
            # Break if we made it to the end of the list
            # and do not add to searchlist
            if ncbest>=len(querylist):
                if opts.verbose:
                    print " break 3"
                break
            
            searchlist.append(cbest)
            lpos=ncbest
            if opts.verbose:
                print "   Now at lpos=%d adding %s %d" \
                      % (lpos,cbest,len(searchlist))
        print "Case #%d: %d" % (count,len(searchlist))

if __name__ == "__main__":
    # Process command line
    # Process it here so opts and args are global
    (opts,args)=process_args()    
    sys.exit(main())
