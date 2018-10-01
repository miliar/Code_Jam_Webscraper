def num_to_list(A):
    result = []
    while A > 0:
        digit = A % 10
        A = A // 10
        result.append(digit)
    result.reverse()
    return result


def list_to_num(l):
    result = 0
    for x in l:
        result *= 10
        result += x
    return result

def shuffle(l):
    sz = len(l);
    return [ l[i:] + l[:i] for i in range(sz)]

def recycle_set(n):
    l = num_to_list(n);
    ll= shuffle(l);
    return map(list_to_num,ll)

    

def solve(A,B):
    N = [0] * (B-A + 1)
    comp = 1
    s = 0

    for i in range(A,B+1):
        idx = i - A
        if N[idx] != 0:
            continue
        else:
            nums = { x for x in recycle_set(i) if x >= A and x<= B }
            for x in nums:
                assert N[x-A] == 0;
                N[x-A] = comp;
            sz = len(nums)
            s += (sz * (sz - 1)) // 2
    return s;


if __name__ == "__main__":
    T = int(input());
    for c in range(T):
        (A,B) = [ int(a) for a in input().strip().split() ]
        R = solve(A,B)
        print("Case #{}: {}".format(c+1,R))


