def main():
    t = int(input())  # read a line with a single integer
    for case in range(1, t + 1):
        print("Case #{}: ".format(case), end="")
        s = input()
        s = [int(x) for x in list(s)]
        if len(s) == 1:
            print(s[0])
        else:
            for i in range(len(s) - 1, 0, -1):
                if s[i-1] > s[i]:
                    s[i-1] -= 1
                    for j in range(i, len(s)):
                        s[j] = 9
            i = 0
            if s[0] == 0:
                i = 1
            while i < len(s):
                print(s[i], end="")
                i += 1
            print("")

if __name__ == '__main__':
    main()