#! /usr/bin/env python

from bisect import bisect

def main():
    with open('d.in', 'r') as fin, open('d.out', 'w') as fout:
        num_cases = int(fin.readline())
        for case in range(1, num_cases + 1):
            num_blocks = int(fin.readline())
            naomis_blocks = sorted(map(float, fin.readline().split()))
            kens_blocks = sorted(map(float, fin.readline().split()))
            war_score = war(naomis_blocks, kens_blocks[:])
            deceit_score = deceitful_war(naomis_blocks[:], kens_blocks[:])
            fout.write('Case #{0}: {1} {2}\n'.format(case, deceit_score, war_score))
    return

def war(p1, p2):
    """Return p1's score in standard game of war."""
    war_score = 0
    for block in p1:
        insert_position = bisect(p2, block)
        if insert_position == 0: # block < x for each x \in p2
            p2.pop(0)
        elif insert_position == len(p2): # block > x for each x \in p2
            p2.pop(0)
            war_score += 1
        else: # pop off the lowest p2 block that is larger than x
            p2.pop(insert_position)
    return war_score

def deceitful_war(p1, p2):
    """Return p1's score in deceitful game of war."""
    war_score = 0
    for block in p1:
        if block < p2[0]: # Use this to pop p2's heaviest block
            p2.pop()
        else:
            p2.pop(0)
            war_score += 1
    return war_score

if __name__ == '__main__':
    main()
