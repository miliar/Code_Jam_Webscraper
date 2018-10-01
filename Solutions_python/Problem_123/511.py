from math import *
def probA():
    f=open('input.txt','r')
    new=open('answer.txt','w')
    for tc in xrange(1, int(f.readline())+1):
        # Get input
        line1=f.readline()
        array=line1.split(" ")
        A=int(array[0])
        N=int(array[1])
        line2=f.readline()
        numbers=[int(x) for x in line2.split(" ")]
        numbers.sort()

        solution=solve(A,numbers)
        
        new.write('Case #%d: %d\n' % (tc, solution))
        
def solve(A,numbers):
    if (len(numbers)==0):
        return 0
    if (A>numbers[0]):
        return solve(A+numbers[0],numbers[1:])
    if (A==1):
        return solve(A,numbers[1:])+1
    add=solve(2*A-1,numbers)+1
    remove=solve(A,numbers[1:])+1
    
    return min(add, remove)
