import sys

def solve(arr, k):
    count = 0
    for i in xrange(len(arr)-k+1):
        if not arr[i]:
            count += 1
            for j in xrange(k):
                arr[i+j] = not arr[i+j]
    if not all(arr):
        return 'IMPOSSIBLE'
    return str(count)

def convert(arr):
    return [x == '+' for x in arr]

def ans(s, k):
    return solve(convert(s), k)

def main():
    T = int(sys.stdin.readline().strip())
    for i in xrange(T):
        s, k = sys.stdin.readline().strip().split(' ')
        k = int(k)
        print('Case #{}: {}'.format(i+1, ans(s,k)))

if __name__ == '__main__':
    main()
