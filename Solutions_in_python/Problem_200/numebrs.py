for t in range(int(input())):
    print("Case #%s: " % str(t + 1), end="")
    n = input()
    for i in range(len(n) - 1):
        if n[i] > n[i + 1]:
            if all(c == '1' for c in n[:i+1]):
                n = '9' * (len(n) - 1)
            else:
                while i > 0 and n[i] == n[i - 1]:
                    i -= 1
                n = n[:i] + str(int(n[i]) - 1) + '9' * (len(n) - i - 1)
            break
    print(n)
