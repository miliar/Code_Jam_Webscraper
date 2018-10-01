from Codejam import codejam_run

@ codejam_run()
def make_me_tidy(N):
    if len(N) == 1:
        return N,

    N = [int(c) for c in N]



    tidy = False

    while not tidy:
        tidy = True
        for i in range(len(N) - 1):
            if N[i] > N[i+1]:
                tidy = False
                N[i] = N[i] - 1
                N = N[:i+1] + [9] * (len(N) - i - 1)

    res = int("".join([str(i) for i in N]))

    return str(res),
