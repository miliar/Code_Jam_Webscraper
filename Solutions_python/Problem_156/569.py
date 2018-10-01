import sys

def solve():
    tests = int(input())
    for test in range(tests):
        int(input())
        a = list(map(int, input().split()))
        result = 1111111
        for maxvalue in range(1, 1111):
            sub = 0
            for val in a: sub += val//maxvalue - 1 if val % maxvalue == 0 else val//maxvalue
            result = min(result, sub+maxvalue)
        print("Case #" + str(test+1)+": "+str(result))

    
def run():
    if sys.hexversion == 50594544 :
        sys.stdin = open("test.txt")
        sys.stdout = open("b.txt", 'w')
    solve()

run()