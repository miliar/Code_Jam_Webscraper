import os
from operator import itemgetter

def get_samples():
    return [os.path.join('in', filename) for filename in os.listdir('in')]

def get_input(path):
    with open(path, 'r') as f:
        return f.readlines()

def write_file(filename, content):
    path = os.path.join('out', filename[3:] + '.out')
    with open(path, 'w+') as f:
        return f.writelines(content)

def parse_input(ar):
    res = []
    i = 1
    for _ in range(int(ar[0])):
        res.append(zip(['R', 'O', 'Y', 'G', 'B', 'V'], map(int, ar[i].split()[1:])))
        i+=1
    return res

def algo(data):
    return [algo_(t) for t in data]

def algo_(horses):
    res = ""
    horses = sorted(horses, key=itemgetter(1), reverse=True)
    numbers = [x[1] for x in horses]
    if numbers[0] > sum(numbers[1:]):
        return "IMPOSSIBLE"
    last = 0
    res += horses[0][0]
    numbers[0] -= 1
    for _ in range(sum(numbers)):
        max_ = 0
        max_it = 0
        for j in range(6):
            if numbers[j] > max_ and j != last:
                max_ = numbers[j]
                max_it = j
        numbers[max_it] -= 1
        res += horses[max_it][0]
        last = max_it
    return res

def format(result):
    return ["Case #%d: %s\n" % (i+1, x) for i, x in enumerate(result)]


def main():

    for file_ in get_samples():
        input_ = get_input(file_)
        data = parse_input(input_)
        result = algo(data)
        write_file(file_, format(result))



if __name__ == '__main__':
    main()
