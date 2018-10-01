namer = "A-large.in"
namew = "A-large.out"
r = open(namer, "r")
w = open(namew, "w")


def N_sub(A):
    N_sub = 0
    for i in range(0, len(A)):
        N_sub = N_sub + A[i]
    return N_sub
        
def Add(A, N_sub):
    Ap = A
    for i in range(0, len(Ap)):
        S = (len(Ap)-1-i)
        N_sub = N_sub - Ap[S]
        if N_sub >= (S):
            pass
        else:
            Ap[0] = Ap[0] + (S - N_sub)
            N_sub = N_sub + (S - N_sub) #So N_sub = S
    return Ap


T = ""
while True:
    c = r.read(1)
    if c != "\n":
        T = T + c
    else:
        break
T = int(T)
print(T)



for i in range(1, T+1):

    S_max = ""
    while True:
        c = r.read(1)
        if c != " ":
            S_max = S_max + c
        else:
            break
    S_max = int(S_max)
    print(S_max)

    S = []
    while True:
        c = r.read(1)
        if c != "\n":
            c = int(c)
            S.append(c)
        else:
            break
    print(S)

    Sp = S[0]
    S1 = Add(S, N_sub(S))
    I = S1[0] - Sp
    print(I)
    out = "Case #"+str(i)+": "+str(I)+"\n"
    w.write(out)
    
r.close()
w.close()
