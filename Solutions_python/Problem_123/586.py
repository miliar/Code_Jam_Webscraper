def readFile(file):
    name = file[:file.index('.')]
    ##print(name)
    f = open(file)
    fout = open(name+'.out','w')
    cases = int(f.readline().strip())
    for case in range(cases):
        a,n = [int(x) for x in f.readline().split()]
        nList = [int(x) for x in f.readline().split()]
        
        result = execute(case,a,n,nList)
        print(result)
        fout.write(result)

def execute(index,a,n,nList):
    print(index,a,n,nList)
    count = 0

    nList.sort()
    count = solve(a,nList[:])
             
    return ''.join(['Case #',str(index+1),': ',str(count),'\n'])

def solve(a,nList):
    #print(a,nList)
    if len(nList) == 0:
        return 0

    nx = nList[0]
    if nx < a:
        a += nx
        return solve(a,nList[1:])
    else:
        if a-1 > 0:
            add = solve(2*a-1,nList[:])
            #remove = len(nList)
            #if add < remove:
            remove = solve(a,nList[1:])
            return 1 + min(add,remove)
        else:
            return 1 + solve(a,nList[1:])
        

if __name__ == "__main__":
    readFile('A-small-attempt1.in')
