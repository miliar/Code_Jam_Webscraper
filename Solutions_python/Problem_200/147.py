t = int(input())  # read a line with a single integer
for k in range(1, t + 1):
  
    n = [int(d) for d in list(raw_input())]

    for i in range(len(n) - 2, -1, -1):
        if n[i] > n[i + 1]:
            n[i] -= 1
            for j in range(i + 1, len(n)):
                n[j] = 9

    while len(n) > 1 and n[0] == 0:
        n = n[1:]

    print("Case #{}: {}".format(k, ''.join([str(d) for d in n])))
    # check out .format's specification for more formatting options


