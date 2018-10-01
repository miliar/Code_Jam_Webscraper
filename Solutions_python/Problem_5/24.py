import sys
import subprocess

# def dimacs(n, customerPrefs):
#     yield 'p cnf %d %d' % (n, len(customerPrefs))
#     yield ' '.join(str(pref[0]) if pref[1] else str(-pref[0]))

# def sat(n, customerPrefs):
#     formula = '\n'.join(dimacs(n
        
# def rsat(dimacs):
#     subprocess.Popen('')

def ok(n, maltedness, customerPrefs):
    for clause in customerPrefs:
        for (bit, state) in clause:
            if int(bool(maltedness & (1 << (bit-1)))) == state:
                break
        else:
            return False
    return True

def format(n, num):
    return ' '.join(str(int(bool(num & (1<<bit)))) for bit in range(n))

def popcount(n):
    def clos(num):
        return sum(map(int, format(n, num).split()))
    return clos

c = input()
for ci in range(1, c+1):
    n = input()
    m = input()
    customerPrefs = []
    for mi in range(m):
        rawprefs = map(int, sys.stdin.readline().split()[1:])
        prefs = set((rawprefs[2*i], rawprefs[2*i+1]) for i in range(len(rawprefs)/2))
        customerPrefs.append(prefs)
    #possible, answer = sat(n, customerPrefs)
    solutions = [maltedness for maltedness in range(1<<n)
                 if ok(n, maltedness, customerPrefs)]
    print 'Case #%d: %s' % (ci, format(n, min(solutions, key=popcount(n)))
                            if solutions else 'IMPOSSIBLE')
