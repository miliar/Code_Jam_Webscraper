import math

def stall(n, k):
    if n == k:
        return 0, 0
    if k == 1:
        return n//2, n//2 - (n % 2 == 0 )
    if n % 2 == 1:
        return stall(n//2, k//2)
    if k % 2 == 0:
        return stall(n//2, k//2)
    return stall(n//2 - 1, k//2)
            
    





def main():
    T = int(input())
    for i in range(1, T + 1):
        n, k = [int(s) for s in input().split(' ')]
        print("Case #{}: {} {}".format(i, *stall(n, k)))


if __name__ == "__main__":
    main()
