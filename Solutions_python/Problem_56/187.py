import sys
from multiprocessing import Pool

def conv(line):
    d = []
    for c in line:
        if c == ".":
            d.append(0)
        elif c == "R":
            d.append(1)
        elif c == "B":
            d.append(2)
        else:
            break
    return d

def findK(k, rotate):
    t = [[0 for i in range(len(rotate[0]))] for j in range(len(rotate))]
    winner = 0
    for j in range(len(rotate)):
        row = rotate[j]
        for i in range(len(row)):
            if row[i] != 0 and row[i] != winner:
                if t[j][i] & 1 == 0:
                    p = 1
                    f = 0
                    while j + p < len(rotate):
                        if rotate[j+p][i] != row[i]:
                            f = 1
                            break
#                        t[j+p][i] |= 1
                        if p == k-1: 
                            if winner == 0:
                                winner = row[i]
                            else:
                                return 3
                            f = 0
                            break
                        p += 1
                    else:
                        f = 2
                    if f == 0:
                        continue
                if t[j][i] & 2 == 0:
                    p = 1
                    f = 0
                    while i + p < len(rotate[j]):
                        if rotate[j][i+p] != row[i]:
                            f = 1
                            break
#                        t[j][i+p] |= 2
                        if p == k-1: 
                            if winner == 0:
                                winner = row[i]
                            else:
                                return 3
                            f = 0
                            break
                        p += 1
                    else:
                        f = 2
                    if f == 0:
                        continue
                if t[j][i] & 4 == 0:
                    p = -1
                    q = 1
                    f = 0
                    while i + p > 0 and j + q < len(rotate):
                        if rotate[j+q][i+p] != row[i]:
                            f = 1
                            break
#                        t[j+q][i+p] |= 4
                        if q == k-1: 
                            if winner == 0:
                                winner = row[i]
                            else:
                                return 3
                            f = 0
                            break
                        p -= 1
                        q += 1
                    else:
                        f = 2
                    if f == 0:
                        continue
                if t[j][i] & 8 == 0:
                    p = 1
                    q = 1
                    f = 0
                    while i + p < len(rotate[j]) and j + q < len(rotate):
                        if rotate[j+q][i+p] != row[i]:
                            f = 1
                            break
#                        t[j+q][i+p] |= 8
                        if q == k-1: 
                            if winner == 0:
                                winner = row[i]
                            else:
                                return 3
                            f = 0
                            break
                        p += 1
                        q += 1
                    else:
                        f = 2
                    if f == 0:
                        continue
    return winner
                    

def main(k, d):
    n = len(d)
    rotate = []
    for l in d:
        if sum(l) == 0:
            continue
        while True:
            try:
                l.remove(0)
            except:
                break
        while len(l) < n:
            l.insert(0, 0)
        rotate.append(l)
    rotate.reverse()
    rotate = zip(*rotate)
    for row in rotate[:]:
        if sum(row) == 0:
            rotate.remove(row)
    d = findK(k, rotate)
    if d == 0:
        return "Neither"
    elif d == 1:
        return "Red"
    elif d == 2:
        return "Blue"
    elif d == 3:
        return "Both"
    
if __name__ == "__main__":
    f = open(sys.argv[1])
    T = int(f.readline())
    data = []
    K = []
    for i in range(T):
        n, k = map(int, f.readline().split())
        K.append(k)
        d = []
        for j in range(n):
            d.append(conv(f.readline()))
        data.append(d)
        
    pool = Pool()
    l = map(main, K, data)
    for i in range(T):
        print "Case #%d: %s" % (i+1, l[i]) 
    