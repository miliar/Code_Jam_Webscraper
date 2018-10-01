def solve(candy):
    #print(candy)
    p = 0
    for c in candy:
        p ^= c
    if p == 0:
        return sum(candy) - min(candy)
    else:
        return "NO"

def main():
    T = int(input())
    for i in range(1, 1 + T):
        N = int(input())
        candy = list(map(int, input().split()))
        ans = solve(candy)
        print("Case #%d: %s" % (i, ans))

if __name__ == "__main__":
    main()


