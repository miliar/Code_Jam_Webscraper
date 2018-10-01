from sys import stdin

def get_answer():
    parts = stdin.readline().strip().split()
    s = [el for el in parts[0]]
    k = int(parts[1])
    flips = 0
    for i in range(len(s) - k + 1):
        if s[i] == "-":
            flips += 1
            for j in range(i, i + k):
                s[j] = "+" if s[j] == "-" else "-"
    for i in range(len(s) - k, len(s)):
        if s[i] == "-":
            return "IMPOSSIBLE"
    return flips


def main():
    t = int(stdin.readline().strip())
    for i in range(t):
        print "Case #{0}: {1}".format(i + 1, get_answer())

if __name__ == "__main__":
    main()
