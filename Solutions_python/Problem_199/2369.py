
def flip(ch):
    if ch == '+':
        return '-'
    else:
        return '+'


def main():
    t = int(input())  # read a line with a single integer
    for case in range(1, t + 1):
        print("Case #{}: ".format(case), end="")
        count = 0
        impossible = False
        s, k = input().split(" ")  # read a list of integers, 2 in this case
        s = list(s)
        k = int(k)
        for i in range(0, len(s) - k + 1):
            if s[i] == '-':
                for j in range(k):
                    s[i+j] = flip(s[i+j])
                count += 1

        for i in range(len(s) - k + 1, len(s)):
            if s[i] == '-':
                impossible = True
                break
        if impossible:
            print("IMPOSSIBLE")
        else:
            print(count)

if __name__ == '__main__':
    main()