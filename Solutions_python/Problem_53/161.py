'''
Created on 8 May 2010

@author: Jirasak.Chirathivat
'''

def simpleFunction(n):
    value = 0
    for i in range(0, n):
        value += (value + 1)
    return value

def checkOnOrOff(n, k):
    t = simpleFunction(n)
    if (k + 1) % (t + 1) == 0:
        return True
    return False

if __name__ == '__main__':
    readfile = file('a.in')
    lines = readfile.readlines()
    
    i = 1
    for line in lines[1:]:
        n, k = [int(x) for x in line.strip().split(' ')]
        value = checkOnOrOff(n, k)
        print 'Case #%s: %s' % (i, 'ON' if value else 'OFF')
        i += 1 
    
    readfile.close()
