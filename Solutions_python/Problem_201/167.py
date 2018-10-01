#Henry Maltby
#Code Jam 2017

def floor_weird(n):
    """
    Returns the largest integer of form 2^k-1 that is < n. Assumes n >= 1. 
    Awful implementation. Awful runtime.
    """
    ans = 2
    while ans < n:
        ans *= 2
    trial = ans - 1
    if trial < n:
        ans = trial
    else:
        ans = (ans // 2) - 1
    return ans

def bathroom_stalls(n, k):
    """
    We can easily determine the behavior of the described process for a fixed 
    N at a given value K when that value K is near a power of 2.
    """
    b = floor_weird(k)
    q, r = divmod(n - b, b + 1)
    if k - b <= r:
        ans = q + 1
    else:
        ans = q
    ans -= 1
    a = ans // 2
    if ans % 2 == 0:
        return [a, a]
    return [a + 1, a]

def C():
    """
    Runs the problem as dictated in problem spec.
    """
    f = open('C-large.in')
    g = open('C-large.out', 'w')

    T = int(f.readline())
    for i in range(T):
        N, K = f.readline().strip().split(' ')
        ans = " ".join([str(x) for x in bathroom_stalls(int(N), int(K))])
        g.write("Case #" + str(i + 1) + ": " + ans)
        if i != T - 1:
            g.write("\n")

C()
