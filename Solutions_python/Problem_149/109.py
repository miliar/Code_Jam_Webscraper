#!/usr/bin/python
import sys
import math
import heapq 
import fractions
import copy
import argparse
import IPython
import ipdb

sys.setrecursionlimit(5000)

author="@".join(["bobp"+"fled","gmail.com"])

class solver:
    """ implements case specific code """
    def __init__(self):
        global pc
        self.pc = pc

    def parse(self):
        [self.n]=map(int,getline().split());
        self.alist=map(int,getline().split());

    def bubble(self,blist):
        ret=0
        progress=True
        debug("bubble",blist)
        while(progress):
            progress=False
            for i in range(len(blist)-1):
                    if(blist[i]>blist[i+1]):
                        (blist[i],blist[i+1])=(blist[i+1],blist[i])
                        ret+=1
                        progress=True
        debug("bubble returns",ret)
        return ret

    def solve(self):
        maxval=reduce(lambda a,b:max(a,b),self.alist)
        ret=self.bubble(list(self.alist))
        for i in range(0,1<<self.n):
            blist=list(self.alist)
            for entry in range(self.n):
                if((i>>entry)&1):
                    blist[entry]=(1<<31)-blist[entry]
            ret=min(ret,self.bubble(blist))
        return ret
            

class precomputer:
    """ 
    implements code that is not case specific such as generating a large
    table that can be used by all testcases
    """
    def __init__(self):
        debug("precomputer.__init__()",level=5)

def main():
    [cases]=map(int,getline().split());
    for caseid in range(1,cases+1):
        docase=(args.testcase is None or caseid in args.testcase)
        if docase:
            debug("Start Case:",caseid,level=5)
        s=solver()
        s.parse()
        if docase:
            debug("Solving Case:",caseid,level=5)
            result=s.solve()
            putline("Case #"+str(caseid)+": "+str(result))

def getline():
    line=args.infile.readline()
    debug("input:",line,level=5,nl=0)
    return line
    

def putline(*arg,**keywords):
    try:
        nl=keywords["nl"];
    except KeyError:
        nl=1
    line=" ".join(map(str,arg))
    if(nl):
        line+='\n'
    args.outfile.write(line)
    debug("output:",line,level=5,nl=0)

def put(*arg):
    putline(*arg,nl=0)

def debug(*arg,**keywords):
    try:
        level=keywords["level"];
    except KeyError:
        level=10
    try:
        nl=keywords["nl"];
    except KeyError:
        nl=1
    if(args.debug>=level):
        args.dbgfile.write(' '.join(map(str,arg)))
        if(nl):
            args.dbgfile.write('\n')

def doargs(argv=sys.argv[1:]):
    global args
    parser=argparse.ArgumentParser(description="solution by "+author)
    parser.add_argument("infile",nargs='?',type=argparse.FileType("r"),default=sys.stdin)
    parser.add_argument("outfile",nargs='?',type=argparse.FileType("w"),default=sys.stdout)
    parser.add_argument("-t",'--testcase',type=int,action="append")
    parser.add_argument("-d",'--debug',type=int,default=8)
    parser.add_argument("-i",'--interactive',action="store_true")
    parser.add_argument("-ipdb","--ipdb",action="store_true")
    parser.add_argument("dbgfile",nargs='?',type=argparse.FileType("w"),default=sys.stderr)
    args=parser.parse_args(argv)

def cleanup():
    if(args.infile!=sys.stdin):
        args.infile.close()
    if(args.outfile!=sys.stdout):
        args.outfile.close()
    if(args.dbgfile!=sys.stderr):
        args.dbgfile.close()

def setup():
    global pc
    try:
        pc
    except NameError:
        pc=precomputer()
    pass;

def run(argstring=None):
    if(not argstring is None):
        doargs(argstring.split())
    if(args.ipdb):
        ipdb.set_trace()
    setup()
    main()
    cleanup()
    if(args.ipdb):
        ipdb.set_trace()

if __name__=="__main__":
    from IPython.core import ultratb
    sys.excepthook = ultratb.FormattedTB(mode='Verbose',color_scheme='Linux', call_pdb=1)
    doargs()
    setup()
    if(args.interactive):
        IPython.embed()
    else:
        run()
