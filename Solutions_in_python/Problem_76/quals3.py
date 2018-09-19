'''
Created on 07/05/2011

@author: German
'''

def sum_xor(xs):
    s = 0
    for x in xs:
        s = s ^ x
    return s

def best_split(parsed_case):
    parsed_case.sort()
    sean = parsed_case[1:]
    patrick = parsed_case[:1]
    while len(sean)>0 and sum_xor(sean) != sum_xor(patrick):
        patrick.append(sean[0])
        sean = sean[1:]
    if len(sean) == 0:
        return None
    else:
        return sum(sean)
        

if __name__ == '__main__':
    with open('sol.out', 'w') as out:
        with open('C-large.in', 'r') as f:
            T = int(f.readline())
            for i in xrange(1,T+1):
                N = int(f.readline().split()[0])
                case = f.readline().split()
                parsed_case = [ int(n) for n in case]
                
                res =best_split(parsed_case)
                                
                res_str = "Case #%d: %s\n" % (i, 'NO' if res is None else str(res))
                print res_str,
                out.write(res_str)