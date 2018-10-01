#main here
infile = open("B-small-attempt0.in", "r")
outfile = open("Bout.txt", "w")
t = int(infile.readline().rstrip())
for z in range(1, t+1):
    #IO here
    raw = infile.readline().split()
    A, B, K = int(raw[0]), int(raw[1]), int(raw[2])
    solution=0
    for i in range(0, A):
        for j in range(0, B):
            output = i&j
            if output<K:
                solution+=1

    #output here
    output = "Case #"+str(z)+": "+str(solution)+'\n'
    print(output)
    outfile.write(output)

infile.close()
outfile.close()
