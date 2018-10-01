

# fin = open("A-small-attempt3.in", "r")
fin = open("A-large.in", "r")
# fout = open("A-small-attempt3.out", "w")
fout = open("A-large.out", "w")


def flip(lists):
    for ind2, el in enumerate(lists):
        if lists[ind2] == "+":
            lists[ind2] = "-"
        else:
            lists[ind2] = "+"
    return lists

def all_same(list):
    pivot = list[0]
    is_ok = True
    for el in list:
        if el != pivot:
            is_ok = False
            break
    return is_ok

testcases = fin.readline()
for index, line in enumerate(fin.readlines()):
    line= line.rstrip("\n")
    chars = list(line.split()[0])
    k = int(line.split()[1])
    if len(chars) == k and not all_same(chars):
        fout.write("Case #{0}: IMPOSSIBLE\n".format(index+1))
        continue
    moves = 0
    is_possible = True
    last_char = len(chars) - k
    for ind, symbol in enumerate(chars):
        if symbol == "-":
            chars[ind:ind+k] = flip(chars[ind:ind+k])
            moves += 1
        if ind == last_char:
            if all_same(chars):
                fout.write("Case #{0}: {1}\n".format(index+1, moves))
            else:
                fout.write("Case #{0}: IMPOSSIBLE\n".format(index+1))
            break


fin.close()
fout.close()

