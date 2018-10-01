def optimal(N, K, cakes):
    r = [cake[0] for cake in cakes]
    h = [cake[1] for cake in cakes]
    surf =  [i ** 2 for i in r]
    side = [2 * a * b for (a, b) in zip(r, h)]
    cakes_sorted = []
    for i in range(N):
        cakes_sorted.append((r[i],h[i],surf[i],side[i]))
    cakes_sorted.sort(reverse=True)
    area = 0
    for i in range(N):
        tmp = sorted(cakes_sorted[i+1:], key = lambda x:x[3], reverse = True)
        tmp2 = cakes_sorted[i][2] + cakes_sorted[i][3] + sum([q[3] for q in tmp[:K-1]])
        area = max(area, tmp2)
    return area


pi = 3.14159265359
import sys

def main():

    num = int(input())
    for i in range(1, num + 1):
        N, K = [int(a) for a in input().split(' ')]
        pancakes = []
        for j in range(0, N):
            pancakes.append([int(cake) for cake in input().split(' ')])
        s2 = optimal(N, K, pancakes)
        print("Case #{}: {}".format(i, s2 * pi))

if __name__ == "__main__":
    main()

