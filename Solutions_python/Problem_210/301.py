#!python
import sys

def solve(nc, nj, cam, jai):
    if nc+nj == 1:
        return 2
    if nc == 0:
        return busy(jai)
    if nj == 0:
        return busy(cam)    
    return 2
    

def busy(act):
    if act[1][1] - act[0][0] <= 720:
        return 2
    if act[1][0] - act[0][1] >= 720:
        return 2
    return 4
    
def main():
    t = int(input())
    for c in range(1, t + 1):
        nc, nj = map(int, input().split(' '))
        cam = []
        jai = []
        for _ in range(nc):
            s, e = map(int, input().split(' '))
            cam.append((s,e, 0))
        for _ in range(nj):
            s, e = map(int, input().split(' '))
            jai.append((s,e, 1))
            
        res = solve(nc, nj, sorted(cam), sorted(jai))
        print('Case #%d: %d' % (c, res))
    
if __name__ == "__main__":
  sys.setrecursionlimit(10000)
  main()
    