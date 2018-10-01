__author__ = 'Reuben'


def solution1(m): #don't forget parameters
    return sum([max(m[i-1]-m[i],0) for i in range(1,len(m))])
def solution2(m):
    M = max([m[i-1]-m[i] for i in range(1,len(m))])
    return sum([min(m[i],M) for i in range(0,len(m)-1)])

f_in = open('file3.in')
f_out = open('file.out','w')

cases = int(f_in.readline()) #first line is always number of cases
for i in range(1,cases+1):
    f_in.readline()
    m = [int(i) for i in f_in.readline().split()]
    s1 = solution1(m)
    s2 = solution2(m)
    f_out.write("Case #"+str(i)+": "+str(s1)+" "+str(s2)+"\n")