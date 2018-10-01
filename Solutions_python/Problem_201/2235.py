'''
Created on 2017-04-08

@author: qiuyx
'''
import math

def solve(N, K):
    a = int(math.log(K,2))
    b = K - (1<<a) + 1
    
    temp = N - (1<<a) + 1
    q = (temp) >> a
    r = temp % (1 << a)
    
    if r < b:
        return [ q/2, (q-1)/2]
    else:
        return [ (q+1)/2 , q/2]

if __name__ == '__main__':
    # read file:
    
    file_in = open('H:/C-small-1-attempt1.in')
    file_out = open('H:/small_output.out', 'w')
    T = int(file_in.readline()[:-1])
    for i in xrange(T):
        
        line = (file_in.readline())[:-1].split(' ')
        N, K = line
        res = solve(int(N), int(K))
        result = 'Case #' + str(i+1) + ': ' + str(res[0]) + ' ' + str(res[1])
        file_out.write(str(result)+'\n')
        print result

    file_out.close()
    file_in.close()
    
