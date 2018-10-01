T = int(input())

for t in range(T):
    Ns = input()
    N = int(Ns)

    for i in range(2, len(Ns) + 1):
        if Ns[-i] > Ns[-i + 1]:
            N -= N%(10**(i-1)) + 1
            Ns = str(N)

    print("Case #{}: {}".format(t+1, Ns))
