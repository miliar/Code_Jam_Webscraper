def solve():
    s, k = input().split()
    k = int(k)
    ans = 0
    for i in range(len(s) - k + 1):
        if s[i] == '-':
            ans += 1
            s = s[:i] + s[i:i+k].replace('+', '*').replace('-', '+').replace('*', '-') + s[i + k:]
    return "IMPOSSIBLE" if s.count('-') else ans

def main():
    tests = int(input())
    for test in range(1, tests + 1):
        print('Case #{}: {}'.format(test, solve()))

if __name__ == '__main__':
    main()
