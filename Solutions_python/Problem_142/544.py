#!/usr/bin/env python

import sys


if __name__ == '__main__':
    T = int(sys.stdin.readline())

    
    for i in range(T):
        N = int(sys.stdin.readline())
        
        
        # Store letters
        letters = []
        
        for _ in range(N):
            s = sys.stdin.readline().strip()
            x = [(s[0], 1)]
            
            for c in s[1:]:
                if c == x[-1][0]:
                    x[-1] = (c, x[-1][1] + 1)
                else:
                    x.append((c, 1))
            
            letters.append(x)
        
        
        # Verify that all strings have the same letter sequence
        if len(set(len(x) for x in letters)) > 1:
            print('Case #%d: Fegla Won' % (i + 1))
            continue
        
        valid = True
        
        for j in range(len(letters[0])):
            if len(set(x[j][0] for x in letters)) > 1:
                valid = False
                break
        
        if not valid:
            print('Case #%d: Fegla Won' % (i + 1))
            continue
        
        
        # Count actions needed
        n = 0
        
        for j in range(len(letters[0])):
            a = [x[j][1] for x in letters]
            mean = int(round(1.0 * sum(a) / len(a)))
            n += sum(abs(x - mean) for x in a)
        
        print('Case #%d: %d' % (i + 1, n))
