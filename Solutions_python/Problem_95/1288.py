'''
@author: Peratham
'''

INPUTFILE = 'A-small-attempt1.in'
OUTPUTFILE = 'A-small-attempt1.out'

inDict = ['ejp mysljylc kd kxveddknmc re jsicpdrysi', 'rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd', 'de kr kd eoya kw aej tysr re ujdr lkgc jv']
outDict = ['our language is impossible to understand', 'there are twenty six factorial possibilities', 'so it is okay if you want to just give up']

def readFile():
    file = open(INPUTFILE, 'r')
    text = file.readline()
    tmp = text.split()
    P = tmp[0]
    
    param = []
    param.append(P)
    input = []
    
    text = file.readlines()
    for line in text:
        input.append(line)
    
    file.close()
    del file
    return [param, input]
    
def solve(param, input):
    ans = []
    
    gdict = {'z':'q','o':'e','a':'y','q':'z'}
    for (i, j) in zip(inDict, outDict):
        for (ii, jj) in zip(i, j):
            gdict[ii] = jj
    print gdict.keys(),gdict.values()
    for i in input:
        temp = ''
        for ii in i:
            if ii == '\n': continue
            temp = temp + gdict[ii]
        ans.append(temp)
    return ans

def writeFile(ans):
    file = open(OUTPUTFILE, 'w')
    file.write("Case #1: %s\n" % ans[0])
    file.close()
    
    file = open(OUTPUTFILE, 'a')
    for i in xrange(len(ans) - 1):
        file.write("Case #%d: %s\n" % ((i + 2), ans[(i + 1)]))
        
    file.close()

def main():
    [param, input] = readFile()
    ans = solve(param, input)
    writeFile(ans)

if __name__ == '__main__':
    main()
