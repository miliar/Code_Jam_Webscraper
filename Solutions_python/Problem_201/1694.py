"""Stalls"""
import fileinput
from math import ceil
from heapq import heappush, heappushpop

def main():
    """Main Method"""
    handler = fileinput.input()
    cases = int(handler.readline())
    for case in range(1, cases+1):
        number, people = handler.readline().split()
        number, people = int(number), int(people)
        if number == people:
            print('Case #{case}: 0 0'.format(case=case))
            continue

        heap = []
        longest = -heappushpop(heap, -number) - 1
        for _ in range(1, people + 1):
            best_max = ceil(longest/2)
            best_min = int(longest/2)
            heappush(heap, -best_max)
            longest = -heappushpop(heap, -best_min) - 1

        print('Case #{}: {} {}'.format(case, best_max, best_min))

if __name__ == '__main__':
    main()
