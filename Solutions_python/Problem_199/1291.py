from typing import List
import sys

def solve(data:List[bool], flip:int) -> int:
    counter = 0
    for i in range(len(data)-flip+1):
        if not data[i]: # == '-'
            # flip
            counter += 1
            for j in range(flip):
                data[i+j] = not data[i+j]
    if all(data):
        return counter
    else:
        return 'IMPOSSIBLE'

def parse(prob:str):
    data, flip = prob.split(' ')
    data = [c=='+' for c in data]
    flip = int(flip)
    return {
        'data': data,
        'flip': flip,
    }

def main():
    filename = sys.argv[1]
    with open(filename) as fp:
        num_prob, *data = fp.readlines()
        for idx, prob in enumerate(map(parse, data), start=1):
            result = solve(**prob)
            print(f'Case #{idx}: {result}')

if __name__ == '__main__':
    main()
