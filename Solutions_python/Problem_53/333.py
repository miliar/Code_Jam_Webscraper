

with open("output.txt", "w") as outf:
    with open("input.txt") as f:
        T = int(f.readline().strip())
        for i in range(T):
            ts = f.readline().strip().split()
            n = int(ts[0])
            two_to_the_n = 2 << (n-1)
            #print two_to_the_n
            k = int(ts[1])
            state = "OFF"
            if (k + 1) % two_to_the_n == 0:
                state = "ON"
            outf.write("Case #%d: %s\n" % ((i+1),state))