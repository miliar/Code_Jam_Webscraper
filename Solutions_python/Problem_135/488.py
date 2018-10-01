'''
Created on 13.04.2013

@author: Alex
'''
   
if __name__ == '__main__':
    f = open('in/A-small-attempt0.in', mode='r')
    g = open('out/A-small-attempt0.out', mode='w')
    n = int(f.readline())
    for i in range(1,n+1):
        count = 0
        solution = ''
        pos1 = int(f.readline())
        candidates = []
        for j in range(1,5):      
            l = list(f.readline().split())
            if j == pos1:
                candidates = l
        pos2 = int(f.readline())
        for j in range(1,5):
            l = list(f.readline().split())
            if j == pos2:
                for k in range(0,4):
                    if l[k] in candidates:
                        count += 1
                        solution = l[k]
        if count == 0:                                        
            g.write('Case #' + str(i) + ': Volunteer cheated!\n') 
        elif count == 1:
            g.write('Case #' + str(i) + ': ' + solution + '\n')
        else:
            g.write('Case #' + str(i) + ': Bad magician!\n')
        
        