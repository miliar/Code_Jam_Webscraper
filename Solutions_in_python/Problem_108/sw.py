'''
Created on 27/05/2012

@author: Fantoccini
'''
from multiprocessing import Process, Manager

def mmm(i, j):
    if i > j:
        return j
    return i

def f(ci, res, n, d, vines):
    res[ci] = "NO"
    for i in range(len(vines)):
        dd, ll, kk = vines[i]
        if i == 0:
            kk = dd
        if dd + kk >= d:
            res[ci] = "YES"
            return
        for j in range(i + 1, len(vines)):
            ddd, lll, kkk = vines[j]
            if ddd <= dd + kk and lll + ll >= ddd - dd and kkk < mmm(ddd - dd, lll):
                vines[j] = ddd, lll, mmm(ddd - dd, lll)

if __name__ == '__main__':
    ps = [] 
    manager = Manager()
    fin = open("sw.in", "r")
    fout = open("sw.out", "w")
    t = int (fin.readline())
    res = manager.list(range(t))
    for ci in range(t):
        n = int(fin.readline())
        vines = []
        for i in range(n):
            line = fin.readline()
            nums = line.split(" ")
            d = int(nums[0])
            l = int(nums[1])
            vines.append((d, l, 0))
        d = int(fin.readline())
        p = Process(target=f, args=(ci, res, n, d, vines))
        ps.append(p)
        p.start()
    for ci in range(t):
        ps[ci].join()
        fout.write("Case #" + str (ci + 1) + ": " + str(res[ci]) + "\n")
    fin.close()
    fout.close()
    
