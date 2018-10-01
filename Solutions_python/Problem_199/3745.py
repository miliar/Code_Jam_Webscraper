IMPOSSIBLE = 10 ** 9

def flip(pancakes):
    result = ""
    for ch in pancakes:
        if (ch == '+'):
            result += "-"
        else:
            result += "+"
    return result

def solve(pancakes, S, K):
    count = 0
    newpancakes = pancakes
    for i in range(0, S-K+1):
        if (newpancakes[i] == '-'):
            newpancakes = newpancakes[:i] + flip(newpancakes[i:i+K]) + newpancakes[i+K:]
            count += 1
    for i in range(S-K+1, S):
        if (newpancakes[i] == '-'):
            return IMPOSSIBLE
    return count

fin = open("A-large.in", "r")
fout = open("pancakes-large.out", "w")
lines_list = fin.readlines()
T = int(lines_list[0])
for i in range(0, T):
    pancakes, strK = lines_list[i+1].split()
    K = int(strK)

    result = solve(pancakes, len(pancakes), K)
    if (result >= IMPOSSIBLE):
        result = "IMPOSSIBLE"
    fout.write("Case #{0}: {1}\n".format(i+1, result))

