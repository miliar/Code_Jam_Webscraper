import sys

def get_deceit_score(n_blocks, k_blocks):
    n_low_index, n_high_index = 0, len(n_blocks) - 1
    k_index = len(k_blocks) - 1

    score = 0
    while n_low_index <= n_high_index:
        if n_blocks[n_high_index] > k_blocks[k_index]:
            score += 1
            n_high_index -= 1
            k_index -= 1

        else:
            n_low_index += 1
            k_index -= 1

    return score

def get_war_score(n_blocks, k_blocks):
    k_low_index, k_high_index = 0, len(k_blocks) - 1
    n_index = len(n_blocks) - 1

    score = 0
    while n_index >= 0:
        if n_blocks[n_index] > k_blocks[k_high_index]:
            score += 1
            n_index -= 1
            k_low_index += 1

        else:
            k_high_index -= 1
            n_index -= 1

    return score

def get_result(case, n_blocks, k_blocks):
    res_str = 'Case #{case}: {deceit} {war}'
    n_blocks = sorted(n_blocks)
    k_blocks = sorted(k_blocks)

    deceit_score = get_deceit_score(n_blocks, k_blocks)
    war_score = get_war_score(n_blocks, k_blocks)

    return res_str.format(case=case, deceit=deceit_score, war=war_score)

def main(argv):
    out = open('out.txt', 'w')
    f = open(argv[0], 'r')
    testcases = int(f.readline())

    for case in xrange(testcases):
        f.readline()
        n_blocks = [float(b) for b in f.readline().split()]
        k_blocks = [float(b) for b in f.readline().split()]

        res = get_result(case + 1, n_blocks, k_blocks)
        out.write(res + '\n')

    out.close()
    f.close()

if __name__ == "__main__":
   main(sys.argv[1:])
