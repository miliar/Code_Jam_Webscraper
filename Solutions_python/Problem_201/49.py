import sys
import collections

def output_for(n):
    mid = n // 2
    ls = mid
    rs = n - 1 - mid
    return min(ls, rs), max(ls, rs)

def solve(n, k):
    q = collections.Counter({n: 1})
    while k:
        size, mult = current = max(q.items())
        # print(f"DEBUG processing size={size} mult={mult}")
        del q[size]

        k -= mult
        mid = (size - 1) // 2
        ls = mid
        rs = size - 1 - mid
        if k <= 0:
            return min(ls, rs), max(ls, rs)

        q[ls] += mult
        q[rs] += mult

def main():
    case_count = int(next(sys.stdin))
    for case_number in range(1, case_count + 1):
        n, k = map(int, next(sys.stdin).split())
        min_lsrs, max_lsrs = solve(n, k)
        print(f"Case #{case_number}: {max_lsrs} {min_lsrs}")

if __name__ == "__main__":
    main()
