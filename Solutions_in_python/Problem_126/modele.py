#!/usr/bin/python
from string import lowercase, maketrans, translate

vowels = 'aeiou'
consonants = [_ for _ in lowercase if not _ in vowels]
table = maketrans(vowels, ' ' * len(vowels))

def get_consecutives_consonants(sub):
    sub = translate(sub, table)
    sub = sub.split(' ')
    return max([len(_) for _ in sub])

def compute_n_value(name, n):
    n_value = 0
    len_name = len(name)
    for i in range(len_name-n+1):
        for j in range(i+n, len_name+1):
            sub = name[i:j]
            consecutives_consonants = get_consecutives_consonants(sub)
            if consecutives_consonants >= n:
                n_value += 1
    return n_value


def compute(infile, outfile):
    number_of_test = int(infile.readline()[:-1])
    for indice_of_test in range(number_of_test):
        one_test = infile.readline()[:-1]
        name, n = one_test.split(' ')
        n = int(n)
        n_value = compute_n_value(name, n)
        outfile.write('Case #%i: %i' % (indice_of_test+1, n_value))
        if indice_of_test < number_of_test-1:
            outfile.write('\n')
    outfile.close()

if __name__ == "__main__":
    import sys
    infile = sys.argv[1]
    outfile = infile.split('.')[0] + ".out"
    infile = open(infile)
    outfile = open(outfile, 'wb')
    compute(infile, outfile)
