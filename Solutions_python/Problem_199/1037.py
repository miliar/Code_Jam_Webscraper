
def swap(v):
    if v == '+':
        return '-'
    else:
        return '+'

def check_stove(s, f):
    idx = 0
    n = len(s)
    flips = 0
    
    while idx < n:
        while idx < n and s[idx] == '+':    
            idx += 1
        if idx >= n:
            return flips
         
        if n - idx < f:
            return -1
        for i in range(f):
            s[idx + i] = swap(s[idx + i])
        flips += 1
        idx += 1
        
    return flips
        
if __name__ == "__main__":

    f = open("input.txt")
    lines = f.readlines()
    f.close()
    t = int(lines[0])
    i = 1
    while i <= t:
        s, f = lines[i].strip().split(' ')
        f = int(f)
        s = list(s)
        res = check_stove(s,f)
        res = "IMPOSSIBLE" if res == -1 else res
        print "Case #%d: %s" % (i, res)
        i += 1
