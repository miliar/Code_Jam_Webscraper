import sys

def solve(l):

    added = 0
    laughing = 0
    for shyness,num in enumerate(l):
        if laughing < shyness:
            added += (shyness - laughing)
            laughing += (shyness - laughing)
        laughing += num

    return added

if __name__ == "__main__":

    f = open(sys.argv[1])
    n = int(f.readline().strip())

    for i in range(1, n + 1):

        l = [int(n) for n in f.readline().split()[-1]]

        x = solve(l)

        print('Case #{}: {}'.format(i, x))

