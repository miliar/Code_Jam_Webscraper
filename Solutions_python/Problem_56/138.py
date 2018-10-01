#!/usr/bin/python

def rotate(table):
    n = len(table)
    for i, line in enumerate(table):
        line = [c for c in line if c != '.']
        prefix = (n-len(line))*['.']
        table[i] = prefix + line

def is_good(table, c, k):
    n = len(table)
    key = c * k
    for i, line in enumerate(table):
        test = ''.join(line)
        if key in test:
            return True
    for j in range(n):
        test = ''.join(line[j] for line in table)
        if key in test:
            return True
    for r in range(n):
        test = ''.join(table[s][r+s] for s in range(n-r))
        if key in test:
            return True
    for r in range(n):
        test = ''.join(table[r+s][s] for s in range(n-r))
        if key in test:
            return True
    for r in range(1, n+1):
        test = ''.join(table[r-1-i][i] for i in range(r))
        if key in test:
            return True
    for r in range(n):
        test = ''.join(table[n-1-s][r+s] for s in range(n-r))
        if key in test:
            return True
    return False

if __name__ == '__main__':
    t = int(raw_input())
    for i in range(t):
        n, k = [int(s) for s in raw_input().split()]
        table = []
        for j in range(n):
            table.append(list(raw_input()))
        rotate(table)
        blue = is_good(table, 'B', k)
        red = is_good(table, 'R', k)
        if blue:
            if red:
                answer = 'Both'
            else:
                answer = 'Blue'
        else:
            if red:
                answer = 'Red'
            else:
                answer = 'Neither'
        print 'Case #%d: %s' % (i+1, answer)
