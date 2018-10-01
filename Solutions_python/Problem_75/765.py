import sys
from collections import defaultdict

def add_to_invocation(char, inv, combs):
    if len(inv) == 0:
        return [char]

    if (inv[-1],char) in combs.keys():
        inv[-1] = combs[(inv[-1], char)]
        return inv
    else:
        inv.append(char)
        return inv

def main(f):
    num_cases = int(f.readline().rstrip())
    for case in range(1, num_cases + 1):
        inp = f.readline().split()
        num_combinations = int(inp[0])
        combinations = inp[1:num_combinations + 1]
        combs = {}
        for combination in combinations:
            x, y, z = combination
            combs[(x,y)] = z
            combs[(y,x)] = z
        num_oppositions = int(inp[num_combinations + 1])
        oppositions = inp[num_combinations + 2: num_combinations + num_oppositions + 2]
        opposite = defaultdict(list)
        for opp in oppositions:
            x, y = opp
            opposite[x].append(y)
            opposite[y].append(x)
        length, invocation = inp[num_combinations + num_oppositions + 2:]
        f_set = set()
        f_list = list()
        for pos in range(int(length)):
            f_list = add_to_invocation(invocation[pos],f_list,combs)
            f_set = set(f_list)
            if opposite.has_key(f_list[-1]): 
                for element in opposite[f_list[-1]]:
                    if element in f_set:
                        f_list = []
                        f_set = set()

        print "Case #%d: [%s]"% (case, ", ".join(f_list))

f = open(sys.argv[1])
main(f)
