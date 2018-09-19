from sys import stdin

def main():
    T = int(stdin.readline())
    for i in xrange(T):
        N, K = map(int, stdin.readline().split())
        p = 1 << N
        result = (K % p) == (p - 1)
        print ("Case #%d:" % (i+1)), "ON" if result else "OFF"

main()