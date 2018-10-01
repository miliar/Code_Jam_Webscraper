#!/Library/Frameworks/Python.framework/Versions/3.3/bin/python3.3
# Codejam ID 2994486
# Run with parameter
# -p for preprocessing
# -s for small input
# -l for large input
# -m=<int> for multithreading


from GCJ import GCJ
import re


def parse(infile):
    N = GCJ.readint(infile)
    matrix = [GCJ.readstr(infile).strip() for i in range(N)]
    return N, matrix
    
def solve(data):
    N, strings = data
    order = re.sub(r"([a-z])\1+", r"\1", strings[0])
    cnt_array = [ [] for i in range(len(order))]
    
    for x in strings:
        if re.sub(r"([a-z])\1+", r"\1", x) != order:
            return "Fegla Won"

        last = '#'
        cnt = 0
        i = -1
        for ch in x:
            if ch != last:
                i += 1
                cnt_array[i].append(1)
            else:
                cnt_array[i][-1] += 1
            last = ch
        
    res = 0
    for a in cnt_array:
        av = sum(a) / len(a)
        ha = {}
        for val in a:
            if val in ha:
                ha[val] += 1
            else:
                ha[val] = 1
        cp = sorted( [ [key, val] for (key, val) in ha.items() ] )
        b = sorted([ [abs(av-cp[i][0]), i] for i in range(len(cp)) ] )

        while len(b) > 1:
            cur_dist, cur_index  = b.pop()
            cur_val, cur_cnt = cp[cur_index]
    
            i = cur_index
            if cur_val > av:
                i -=  1
                while cp[i][1] == 0:
                    i -= 1
            else:
                i += 1
                while cp[i][1] == 0:
                    i += 1
            mv_index = i

            res += cur_cnt * (abs(cur_val-cp[mv_index][0]))
            cp[mv_index][1] += cur_cnt
            cp[cur_index][1] = 0

            av = sum(map(lambda y: y[0] * y[1], cp)) / len(a)
            for i in range(len(b)):
                b[i][0] = abs( av - cp[ b[i][1] ][0] )
            b = sorted(b)
            
    return res
            

if __name__ == "__main__":
    GCJ('A', solve, parse, None).run()
