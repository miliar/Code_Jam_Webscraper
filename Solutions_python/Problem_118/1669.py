'''
Created on 13.04.2013

@author: Alex
'''
def isPal(string):
    return string == string[::-1]
    
if __name__ == '__main__':
    lst = []
    for i in range(1, 10000001):
            if i % 10 == 0:
                pass
            elif isPal(str(i)) and isPal(str(i*i)):
                lst.append(i*i)
    f = open('C-large-1.in', mode='r')
    g = open('C-large-1.out', mode='w')
    t = int(f.readline())
    for i in range(0, t):
        line = f.readline()
        a = int(line.split()[0])
        b = int(line.split()[1]) 
        count = 0
        for j in lst:
            if a <= j <= b:
                count += 1
        g.write('Case #' + str(i+1) + ': ' + str(count) + '\n') 