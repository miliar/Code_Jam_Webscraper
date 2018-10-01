'''
Created on Apr 15, 2017

@author: qiuyx
'''

def solve(KS, D):
    
    times = []
    for i in xrange(len(KS)):
        times.append( (D - KS[i][0]) / KS[i][1] )
     
    return (D / max(times))
    
    
if __name__ == '__main__':
    # read file:
    
    file_in = open('H:/1B/A-small-attempt0.in')
    file_out = open('H:/1B/A-small-output.out', 'w')
    T = int(file_in.readline()[:-1])
    for i in xrange(T):
        line = (file_in.readline())[:-1].split(' ')
        D, N = float(line[0]), int(line[1])
        KS= []
        
        for j in xrange(N):
            line = list((file_in.readline())[:-1].split(' '))
            K, S = float(line[0]), float(line[1])
            KS.append([K, S])

        s = solve(KS, D)
        
        result = 'Case #' + str(i+1) + ': ' + str(s) 
        file_out.write(result + '\n')
        print result
 

    file_out.close()
    file_in.close()