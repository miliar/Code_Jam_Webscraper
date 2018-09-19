'''
Created on May 22, 2011

@author: diego
'''



def solve(players,low,high,freqs):
    for x in range(low,high+1):
        testFreqs=freqs[:]
        result=True
        for freq in testFreqs:
            if(x>freq) and (x % freq)!=0:
               result=False
               break
            elif (x<freq) and (freq % x)!=0:
                result=False
                break
        if result:
            return x
    
    return "NO"

if __name__ == '__main__':
    file=open('test.dat')
    lines=file.readlines()
    testCases=int(lines[0])
    lines=lines[1:]
    i=1
    while(len(lines)>0):
       params=lines[0]
       params=params.split()
       players=params[0]
       low=int(params[1])
       high=int(params[2])
       freqs=lines[1]
       freqs=freqs.split()
       freqs=map(lambda x: int(x),freqs)
       
       resp=solve(players,low,high,freqs)
       print 'Case #' + str(i) + ': ' + str(resp)
       lines=lines[2:]
       i=i+1