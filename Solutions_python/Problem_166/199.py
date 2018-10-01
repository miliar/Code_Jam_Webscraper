##input = open('B-sample-input.txt', 'r')
##output = open('B-sample-output.txt', 'w')

input = open('B-small-attempt0.in', 'r')
output = open('B-small.out', 'w')

##input = open('B-large.in', 'r')
##output = open('B-large.out', 'w')

from copy import deepcopy

def read_int():
    return int(input.readline().strip())

def read_ints():
    return [int(x) for x in input.readline().split()]

def read_float():
    return float(input.readline().strip())

def read_floats():
    return [float(x) for x in input.readline().split()]

def solve(k,l,s,keyboard,target):
    lista =[""]
    for i in range(s):
        templist =[]
        for c in keyboard:
            for word in lista:
                templist.append(word + c)    
        lista = deepcopy(templist)
    total = len(lista)
    count = 0
    best = 0
    for word in lista:
##        print 'word =', word
        wordcount = 0
        for i in range(s - l + 1):
##            print 'i=', i
            if word[i:i+l] == target:
                count += 1
                wordcount += 1
        if wordcount > best:
            best = wordcount
##    print 'best =', best
##    print 'count =', count
    return best - (count * 1.0) / len(lista)
        
            
##print solve(7, 6, 6, 'BANANAS', 'MONKEY')

def main():
    num_cases = read_int()
    for case in range(1, num_cases+1):
        k,l,s = read_ints()
        keyboard = input.readline().strip()
        target = input.readline().strip()
##        if case == 1:
        solution = solve(k,l,s,keyboard,target)
        solution_string = "Case #%d: %s" %(case, solution)
        output.write(solution_string + "\n")
        print solution_string
        

main()
input.close()
output.close()
    
