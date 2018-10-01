import sys
import collections


multiplication_table = [
    [1, 'i', 'j', 'k'],
    ['i', -1, 'k', '-j'],
    ['j', '-k', -1, 'i'],
    ['k', 'j', '-i', -1]
]
multiplication_table_labels = [1, 'i', 'j', 'k']
neg = {
    1: -1,
    -1: 1,
    'i': '-i',
    '-i': 'i',
    'j': '-j',
    '-j': 'j',
    'k': '-k',
    '-k': 'k'
}


def main():
    mult = collections.defaultdict(dict)
    for x in multiplication_table_labels:
        for y in multiplication_table_labels:
            xi = multiplication_table_labels.index(x)
            yi = multiplication_table_labels.index(y)
            res = multiplication_table[xi][yi]

            mult[x][y] = res
            mult[neg[x]][y] = neg[res]
            mult[x][neg[y]] = neg[res]
            mult[neg[x]][neg[y]] = res

    div = collections.defaultdict(dict)
    for a in range(4):
        for b in range(4):
            res = multiplication_table[a][b]
            x = multiplication_table_labels[a]
            y = multiplication_table_labels[b]
            
            div[res][x] = y
            div[neg[res]][x] = neg[y]
            div[res][neg[x]] = neg[y]
            div[neg[res]][neg[x]] = y


    t = int(sys.stdin.readline())
    for r in range(t):
        l, x = map(int, sys.stdin.readline().strip().split())

        s = sys.stdin.readline().strip() * x

        n = l * x
        success = False
        prefix_mult = [0] * n
        res = 1
        for k in range(n):
            res = mult[res][s[k]]
            prefix_mult[k] = res

        for i in range(n):
            if prefix_mult[i] == 'i':
                for j in range(i + 1, n):
                    mult2 = div[prefix_mult[j]][prefix_mult[i]]
                    mult3 = div[prefix_mult[-1]][prefix_mult[j]]
                    if mult2 == 'j' and mult3 == 'k':
                        success = True
                        break
                if success:
                    break

        print ('Case #%d: %s' % (r + 1, 'YES' if success else 'NO'))

if __name__ == '__main__':
    main()
