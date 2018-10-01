#!python
import sys

def solve(pancakes, k, n):
    if all(pancakes) or len(pancakes) == 0:
        return str(n)
    elif k > len(pancakes):
        return "IMPOSSIBLE"
    elif pancakes[0]:
        return solve(pancakes[1:], k, n)
    else:
        for i in range(k):
            pancakes[i] = not pancakes[i]
        return solve(pancakes, k , n+1)

def main():
    n = int(input())
    for c in range(1, n + 1):
        pancakes, k = input().split(' ')
        pancakes = [c == '+' for c in pancakes]
        k = int(k)
        res = solve(pancakes, k, 0)
        print('Case #%d: %s' % (c, res))
    
if __name__ == "__main__":
  sys.setrecursionlimit(10000)
  main()
    