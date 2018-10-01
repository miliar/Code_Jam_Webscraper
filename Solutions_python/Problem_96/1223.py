'''
@author: Peratham
'''

INPUTFILE = 'B-large.in'
OUTPUTFILE = 'B-large.out'
#INPUTFILE = 'B-toy.in'
#OUTPUTFILE = 'B-toy.out'

def readFile():
    file = open(INPUTFILE, 'r')
    text = file.readline()
    tmp = text.split()
    P = tmp[0]
    
    param = {}
    param['T'] = int(P)
    input = []
    
    num_googler = []
    num_surprise = []
    p_list = []
    text = file.readlines()
    for line in text:
        tmp = line.split()
        num_googler.append(int(tmp[0]))
        num_surprise.append(int(tmp[1]))
        p_list.append(int(tmp[2]))
        input.append(tmp[3:])
        
    param['S'] = num_surprise
    param['p'] = p_list
    param['N'] = num_googler
    
    file.close()
    del file
    return [param, input]

def solve(param, input):
    ans = []
    S = param['S']
    p = param['p']
    N = param['N']
    from math import ceil
    for i in xrange(param['T']):
        if p[i] == 0:
            ans.append(N[i])
            continue
            
        count_pass = 0
        inp = [int(tmp) for tmp in input[i]]
        inp.sort(reverse=True)
        for j in xrange(N[i]):
            if ceil(inp[j] / 3.0) >= p[i]:
                count_pass += 1
                inp[j] = 0
                
        inp.sort(reverse=True)
        for s in xrange(S[i]):
            if ceil(inp[s] / 3.0) + 1 >= p[i] and inp[s] % 3 != 1 and inp[s] > 1:
                count_pass += 1
                inp[s] = 0
        ans.append(count_pass)
    return ans

def writeFile(ans):
    file = open(OUTPUTFILE, 'w')
    file.write("Case #1: %d\n" % ans[0])
    file.close()
    
    file = open(OUTPUTFILE, 'a')
    for i in xrange(len(ans) - 1):
        file.write("Case #%d: %d\n" % ((i + 2), ans[(i + 1)]))
        
    file.close()

def main():
    [param, input] = readFile()
    ans = solve(param, input)
    writeFile(ans)

if __name__ == '__main__':
    main()
