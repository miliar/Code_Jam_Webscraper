import os
global case_runs
case_runs = 1
def format(res):
    global case_runs
    print "Case #" +  str(case_runs) + ":", res
    case_runs += 1


file = open(os.getcwd() + '/' + "input.txt").read().split("\n")
file = file[1:]

phrase = 'welcome to code jam'

for line in file:
    orig = line
    
    arr = []
    count = []
    d = {}
    
    
    for i in range(1, len(phrase)+1):
        arr.append(phrase[:i])
        count.append(0)
    
    for l in line:
        n = phrase.find(l)
        while n != -1:
            if n==0:
                 count[n] += 1
            else:
                count[n] += count[n-1]
            n = phrase.find(l, n+1)
    format(str(count[-1]).zfill(4)[-4:])
    
    

    
