#!/usr/bin/python

def letters_to_ijk(length, repeat, letters, backtrack_i = None, backtrack_j = None, backtrack_level = None):
    if len(letters)!=length:
        raise Exception("Length of letters not matching length")
    
    haystack = 'ijk'
    current = '1'
    negative = False
    found = 0 if backtrack_level is None else backtrack_level + 1
    backtracks = []

    table = {'11' : ['1', False], '1i' : ['i', False], '1j': ['j', False], '1k' : ['k', False],
              'i1' : ['i', False], 'ii' : ['1', True], 'ij': ['k', False], 'ik' : ['j', True],
              'j1' : ['j', False], 'ji' : ['k', True], 'jj': ['1', True], 'jk' : ['i', False],
              'k1' : ['k', False], 'ki' : ['j', False], 'kj': ['i', True], 'kk' : ['1', True]}

    for i in range(repeat):
        if backtrack_i is not None:
            if i < backtrack_i:
#                print("skipping i due to backtrack_i", i, backtrack_i)
                continue
            else:
                backtrack_i = None
        for j, x in enumerate(letters):
            if backtrack_j is not None:
                if j <= backtrack_j:
#                    print("skipping j due to backtrack_j", j, backtrack_j)
                    if j==len(letters)-1:
                        backtrack_j = None
                    continue
                else:
                    backtrack_j = None
            y = table[current + x]
            current = y[0]
            if negative:
                negative = not y[1]
            else:
                negative = y[1]
            if not negative and found<2 and current==haystack[found]:
                current = '1'
                backtracks.append([i, j, found])
                found += 1
    if not negative and found==2 and current==haystack[found]:
        return "YES"
    else:
#        print("backtracks", backtracks)
        for z in reversed(backtracks):
#            print("will backtrack now", z[0], z[1], z[2])
            if letters_to_ijk(length, repeat, letters, z[0], z[1], z[2])=="YES":
                return "YES"
        return "NO"

def main():
    with open('input.in', 'r') as f:
        with open('output.txt', 'w') as o:
            n = int(f.readline().rstrip('\n'))
            for i in range(n):
                length, repeat = list(map(int, f.readline().rstrip('\n').split(' ')))
                letters = f.readline().rstrip('\n')
                result = "Case #" + str(i + 1) + ": " + letters_to_ijk(length, repeat, letters)
                print(result)
                o.write(result + "\n")

if __name__=="__main__":
    main()
