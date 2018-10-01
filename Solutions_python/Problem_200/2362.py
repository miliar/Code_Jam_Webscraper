T = int(input())

for i in range(0, T):

    # Get input
    N = input()
    N2 = N
    N = str(N)
    N = list(N)
    isSorted = True

    index = 0
    # Find first wrong digit
    for j in range(1, len(N)):
        if (N[j] < N[j-1]):
            isSorted = False
            break
        if (N[j] != N[index]):
            index = j
    # Change for 9
    for j in range(index+1, len(N)):
        N[j] = '9'

    #  Minus one
    if(len(N) > 1 and index < len(N)-1):
        N[index] = (str(int(N[index]) - 1))

    if not isSorted:
        N = ''.join(N)
        N = int(N)
        print("Case #" + str(i+1) + ": " + str(N))
    if isSorted:
        print("Case #" + str(i+1) + ": " + str(N2))
