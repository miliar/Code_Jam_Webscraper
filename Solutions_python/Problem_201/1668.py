from sys import stdin
from math import log, pow

def get_answer():
    parts = [int(el) for el in stdin.readline().strip().split()]
    n = parts[0]
    k = parts[1]
    row_num = int(log(k, 2))
    gaps_in_row = int(pow(2, row_num))
    num_in_row = k - gaps_in_row + 1
    min_size = int((n - gaps_in_row + 1) / gaps_in_row)
    count_max = (n - gaps_in_row + 1) % gaps_in_row
    gap_size = min_size + 1 if num_in_row <= count_max else min_size
    min_res = (gap_size - 1) / 2
    max_res = gap_size / 2
    return " ".join([str(max_res), str(min_res)])

def main():
    t = int(stdin.readline().strip())
    for i in range(t):
        print "Case #{0}: {1}".format(i + 1, get_answer())

if __name__ == "__main__":
    main()
