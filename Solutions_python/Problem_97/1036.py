#Google Code Jam 2012
#Qualification Round
#Problem C

from math import floor,log

def file2gen(name):
    f=open(name,'r')
    text=f.read()
    f.close()
    return (line for line in text.splitlines())

def parse(gen):
    cases=int(next(gen))
    tr=[[]]*cases
    for i in range(cases):
        tr[i]=[int(e) for e in next(gen).split()]
    return tr

def rotate(number, digits):
    front=number%(10**digits)
    back=number//(10**digits)
    L=floor(log(back,10))+1
    return front*(10**L)+back

def rotateset(number, size,low, high):
    li=list(set([rotate(number,i) for i in range(size)]))
    return [e for e in li if e<=high and e>=low]

def answer(low,high):
    size=len(str(low))
    total=0
    i=low
    cache=set()
    while i<=high:
        if i not in cache:
            li=rotateset(i,size,low,high)
            for e in li:
                cache.add(e)
            total+=len(li)*(len(li)-1)//2
        i+=1
    return total


def run(infile,outfile):
    cases=parse(file2gen(infile))
    f=open(outfile,'w')
    for i in range(len(cases)):
        f.write('Case #'+str(i+1)+': '+str(answer(cases[i][0],cases[i][1]))+'\n')
    f.close()


if __name__=='__main__': run('C-small-attempt0.in', 'out.txt')

