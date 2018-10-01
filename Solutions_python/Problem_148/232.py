##input = open('A-sample-input.txt', 'r')
##output = open('A-sample-output.txt', 'w')

##input = open('A-small-attempt2.in', 'r')
##output = open('A-small.out', 'w')

input = open('A-large.in', 'r')
output = open('A-large.out', 'w')

def read_int():
    return int(input.readline().strip())

def read_ints():
    return [int(x) for x in input.readline().split()]

def read_float():
    return float(input.readline().strip())

def read_floats():
    return [float(x) for x in input.readline().split()]

    

def search(l, n):  #highest number smaller than a certain amount
##    print l, n
    size = len(l)
    if size == 0:
        return -1
    if l[size-1] <= n:
        return size - 1
    if l[0] > n:
        return -1
    if size == 1:
        return 0
    if size == 2:
        if l[1] > n:
            return 0
        else:
            return 1
    if l[size / 2] > n:
        a = search(l[: size/2], n)
##        print 'a=', a
        return a
    else:
        a = size/2 + search(l[size/2:], n)
##        print 'a=', a
        return a


def solve2(N, X, S):
    S.sort()
    size = len(S)
    discs = 0
    while size > 1:
##        print S
        end = S[-1]
        target = X - end
        answer = search(S[:-1], target)
##        print 'answer =', answer
        S.pop(-1)
##        print S, 'after pop'
        size -= 1
        if answer != -1:
            S.pop(answer)
##            print S, 'after found pop'
            size -= 1
        discs += 1
    if size == 1:
        discs += 1
    return discs
        
##l = [37, 47, 48, 73, 122, 125, 162, 190, 233, 297]
##X = 48
##print l[search(l, X)]
            

def solve(N, X, S):
    S.sort()
    size = len(S)
##    print S, X
    pairs = 0
    end = search(S, X)
    if end == -1:
        return size
    start = 0
    left_marker = -1
    available_pairs = 0
    farthest_end = -1
    found = False
    last_found = -1
    while start < end:
##        print start, end
##        print 'num =', S[end]
        target = X - S[end]
##        print 'target=', target
        find = search(S[start: end], target)
##        print 'find =', find
        if find != -1:
##            print 'found pair', S[find + start]
            last_found = find + start
            pairs += 1
            left_marker = find + start
##            print 'left marker=',left_marker
            farthest_end = end + start
##            print 'farthest end =', farthest_end
            start = find + start + 1
##            print 'start=', start
            end -= 1
##            print 'end=', end
            found = True            
        else:
            if available_pairs > 0:
                pairs += 1
            end -= 1
            found = False
        available_pairs = left_marker - pairs + 1
    
##    print start
    
    if start == end and found:
##        print 'ion here'
        start = left_marker + 1
    else:
        start = left_marker
##    print found
    if found:
        start -= 0
    else:
        start += 1
##    print 'start =', start
##    print 'availables =', available_pairs
    
    potentials = start + 1 - pairs
##    print 'end start=', S[start]
##    print 'availables =', available_pairs
    extras = min(potentials/2, available_pairs)
    if extras <0:
        extras = 0
    pairs += extras
##    print 'pairs =', pairs
    return str(size - pairs)
    
    

def main():
    num_cases = read_int()
    for case in range(1, num_cases+1):
        N, X = read_ints()
        S = read_ints()
##        if case == 91:
        solution = solve(N, X, S)
        solution_string = "Case #%d: %s" %(case, solution)
        output.write(solution_string + "\n")
        print solution_string
        

main()
input.close()
output.close()
    
