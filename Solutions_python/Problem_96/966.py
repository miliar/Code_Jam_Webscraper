# solution for https://code.google.com/codejam/contest/1460488/dashboard#s=p0
import sys
import math

def unsurprising_tuple(score):
    min_score = math.floor(score/3)
    tuple = [min_score, min_score, min_score]
    if (score%3):
        tuple[0] += 1
        if (score%3) == 2:
            tuple[1] += 1
    return tuple

def surprise(tuple, min_score):
    return (tuple[0]+1 >= min_score and tuple[1]-1 >=0 and tuple[0] == tuple[1]) #if tuple[1]-1 >=0 then tuple[2]-1 >=0 is true also

def solve(googlers, surprising, min_score, scores):
    #init
    high_scorers = 0
    for score in scores:
        tuple = unsurprising_tuple(score)
        print score, tuple
        if tuple[0] >= min_score: # maximum value is found at least in first position
            high_scorers += 1
        elif surprising and surprise(tuple, min_score):
            high_scorers += 1
            surprising -= 1
    return high_scorers
    
filename = sys.argv[1] #get filename from arguments
f_in = open(filename,'r')
output = filename.split('.in')[0] + '.out' # generate output filename
f_out = open(output,'w')
n = 0
cases = f_in.readline() #  number of testcases
for n in range(int(cases)):
    line = f_in.readline().rstrip()
    # for each test case do the convertion
    numbers =[int(num) for num in line.split(' ')]
    high_scorers = solve(numbers[0],numbers[1],numbers[2],numbers[3:])
    f_out.write('Case #%d: %d\n' %(n+1, high_scorers))
    print '------- sur:', numbers[1], 'min:', numbers[2], 'scorers', high_scorers