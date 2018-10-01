import sys

def parse_line(line):
    tokens = line.split()
    combo_count = int(tokens[0])
    combos = {}
    if combo_count > 0:
        for i in range(1, combo_count+1):
            first = tokens[i][0]
            second = tokens[i][1]
            result = tokens[i][2]
            if not combos.has_key(first):
                combos[first] = {second: result}
            else:
                combos[first][second] = result
            if not combos.has_key(second):
                combos[second] = {first: result}
            else:
                combos[second][first] = result
            
    clear_count = int(tokens[combo_count+1])
    clears = {}
    if clear_count > 0:
        for i in range(combo_count+2, combo_count+clear_count+2):
            if not clears.has_key(tokens[i][0]):
                clears[tokens[i][0]] = [tokens[i][1]]
            else:
                clears[tokens[i][0]] += [tokens[i][1]]
            
            if not clears.has_key(tokens[i][1]):
                clears[tokens[i][1]] = [tokens[i][0]]
            else:
                clears[tokens[i][1]] += [tokens[i][0]]
    seq = (tokens[-2], tokens[-1])
    return combos, clears, seq        

def solve(i, combos, clears, seq):
    result = []
    for l in seq[1]:
        if len(result) == 0:
            result += [l]
            continue
        if combos.has_key(l):
            if combos[l].has_key(result[-1]):
                result[-1] = combos[l][result[-1]]
                continue
        if clears.has_key(l):
            if len(set(clears[l]).intersection(set(result))) != 0:
                result = []
                continue
        result += [l]
    string = "Case #%d: %s" % (i, result)
    print str.replace(string, "'", "")

if __name__ == '__main__':
    lines = sys.stdin.readlines()
    tests = int(lines[0])
    i = 0
    while i < tests:
        solve(i+1, *parse_line(lines[i+1]))
        i+=1