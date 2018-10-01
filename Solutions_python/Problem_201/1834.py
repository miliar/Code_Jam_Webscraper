from math import log


def findMinMax(n, k):

    if int(log(n, 2)) == int(log(k, 2)):
        return (0, 0)

    a = [False]*n

    for i in range(k):

        left = -1
        right = -1

        for j in range(n):
            if a[j] is False:

                k = j-1
                while k >= 0 and a[k] is False:
                    k -= 1
                current_left = j-1-k

                k = j + 1
                while k <= n-1 and a[k] is False:
                    k += 1
                current_right = k-j-1

                if min(left, right) < min(current_right, current_left):
                    left, right = current_left, current_right
                    pos = j
                elif min(left, right) == min(current_right, current_left):
                    if max(left, right) < max(current_right, current_left):
                        left, right = current_left, current_right
                        pos = j

        a[pos] = True

    return(max(left, right), min(left, right))

t = int(raw_input())
i = 0

while t:

    t -= 1
    i += 1

    n, k = map(int, raw_input().split())

    s = findMinMax(n, k)

    print("Case #{}: {} {}".format(i, s[0], s[1]))
