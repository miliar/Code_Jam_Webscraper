#!python
import sys

def solve(d, horses):
    
    t = max([(d-k)/s for (k, s) in horses])
    return d/t
    

def main():
    t = int(input())
    for c in range(1, t + 1):
        d, n = map(int, input().split(' '))
        horses =[]
        for _ in range(n):
            k, s = map(int, input().split(' '))
            horses.append((k,s))
        res = solve(d, horses)
        print('Case #%d: %f' % (c, res))
    
if __name__ == "__main__":
  sys.setrecursionlimit(10000)
  main()
    