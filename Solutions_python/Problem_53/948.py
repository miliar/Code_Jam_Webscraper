
in_file = open("A-small.in")

input = in_file.read().split("\n")

out_file = open("a.out","w")


for i in range(int(input[0])):
    n, k = input[i + 1].split(" ")
    n, k = int(n), int(k)
    print n, k
    state = {}
    for j in range(n):
        state[j] = 0
    for m in range(k):
        for j in range(n):
            if state[j] == 0:
                state[j] = 1
                break
            else:
                state[j] = 0
                
    t = True
    for j in range(n):
        if state[j] == 0:
            t = False
    if t:
        out_file.write("Case #" + str(i+1) + ": ON\n")
    else: 
        out_file.write("Case #" + str(i+1) + ": OFF\n")
   
out_file.close()
