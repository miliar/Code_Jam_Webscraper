import fileinput

def read_input():
    # gets next line from the file specified as argument or stdin
    # useful to debug within PyCharm, because you can't redirect stdin :-(
    # first time, initialize a function attribute (it's like a static local function in C++)
    # that will keep state across invocations
    if not hasattr(read_input, 'input'):
        read_input.input = fileinput.input()
    return read_input.input.next().strip()


def flip(S):
    return ''.join(['+' if c=='-' else '-' for c in S])

assert flip('+++') == '---'
assert flip('+-+') == '-+-'
assert flip('-++') == '+--'


def solve(S, K):
    flips = 0
    for i in range(0, len(S)-K+1):
        if S[i] == '-':
            S = S[:i] + flip(S[i:i+K]) + S[i+K:]
            flips += 1

    return 'IMPOSSIBLE' if S.count('-') != 0 else str(flips)


if __name__ == "__main__":
    T = int(read_input())
    # sys.stderr.write("%d\n" % (T,))
    for i in xrange(1, T+1):
        S, K = read_input().split()
        K = int(K)
        solution = solve(S, K)
        print("Case #%d: %s" % (i, solution))


