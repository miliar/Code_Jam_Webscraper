import sys

def solve():
    N = sys.stdin.readline().rstrip()

    # Find the first piece of untidyness
    last_clean = -1
    for i in range(len(N)-1):
        if N[i] > N[i+1]:
            break
        elif N[i] < N[i+1]:
            last_clean = i
    else:
        # Number is tidy!
        return N

    # Untidyness happens between position i and i + 1
    prefix = N[:last_clean+2]
    return int(str(int(prefix)-1) + '9' * (len(N)-len(prefix)))

def main():
    T = int(sys.stdin.readline().rstrip())
    for t in range(1, T+1):
        answer = solve()
        print 'Case #{}: {}'.format(t, answer)

if __name__ == "__main__":
    main()
