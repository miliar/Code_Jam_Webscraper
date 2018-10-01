

def main():
    #source = 'A.txt'
    #source = 'A-small-attempt0.in'
    #source = 'A-small-attempt1.in'
    source = 'A-large.in'
    output = source[:-4] + '.out.txt'

    problem = open(source)
    solution = open(output,'w')

    cases = int(problem.next())
    for i in range(1, cases + 1):
        wires = []
        for w in range(int(problem.next())):
            start, end = map(int, problem.next().split())
            wires.append((start, end))
        solution.write('Case #%d: %s\n' % (i, solve(wires)))
    
    problem.close()
    solution.close()

def solve(wires):
    wires.sort()
    crossovers = 0
    for i in range(len(wires)):
        start, end = wires[i]
        for j in range(i + 1, len(wires)):
            other_start, other_end = wires[j]
            # We know other_start > start.
            if other_end < end:
                crossovers += 1
    return crossovers

main()
print 'done'
