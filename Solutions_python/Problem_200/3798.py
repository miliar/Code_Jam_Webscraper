import sys        

def case(n, s):
    print("Case #" + str(n+1) + ": ", end="")
    for i in s:
        print(i, end="")
    print()

Input = open("B-small-attempt0.in", "r")

T = int(Input.readline()[:-1])
for i in range(T):
    N = [l for l in Input.readline()[:-1]]
    while True:
        for j in range(len(N)-1, -1, -1):
            if j > 1:
                if N[j] < N[j-1]:
                    N[j] = "9"
                    N[j-1] = str(int(N[j-1])-1)
                    #print(N)
            if all([N[k] <= N[k+1] for k in range(len(N)-1)]):
                break
            if j == 0:
                N[j] = str(int(N[j])-1)
                for k in range(1, len(N)):
                    N[k] = "9"
                #print(N)
            if all([N[k] <= N[k+1] for k in range(len(N)-1)]):
                break
        if all([N[k] <= N[k+1] for k in range(len(N)-1)]):
            break
    while N[0] == "0":
        N.pop(0)
    case(i, N)
