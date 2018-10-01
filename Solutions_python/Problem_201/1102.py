import math
infile = open("Csmall2.in", "r")
outfile = open("Cout1.txt", "w")

tcase = int(infile.readline().rstrip())
for z in range(1, tcase+1):
    inline = infile.readline().rstrip()
    N, person= inline.split()
    N = int(N)
    person = int(person)
    if N%2 == 0:
        even = 1
        odd = 0
    else:
        even = 0
        odd = 1
    level = 0
    person -= 1
    if N%2 == 0:
        parity = 0
    else:
        parity = 1
    while person > 0:
        oldN = N
        if parity == 1:
            if N%2 == 0:
                N+=1
            if int((N-1)/2) % 2 == 0:
                even += odd*2
        if parity == 0:
            if int((N-1)/2) % 2 == 0:
                even += odd*2
            if N%2!=0:
                N+=1
        if N%2 != 0:
            if int(N/2) % 2 == 0:
                parity = 0
            else:
                parity = 1
        if N%2 == 0:
            if int((N-1)/2+1) % 2 == 0:
                parity = 0
            else:
                parity = 1
        N = int((oldN-1)/2)
        level += 1
        odd = int(math.pow(2,level)-even)
        if person <= math.pow(2, level):
            if parity%2 == 0 and N%2!=0 and person <= even:
                N+=1
            if parity%2 != 0 and person <= odd and N%2==0:
                N+=1
            #print(N, parity, even, odd)
            break
        person -= int(math.pow(2, level))
        #print(level, parity, N, even, odd, person)
    if N == 0:
        N = 1
    if N%2 == 0:
        outfile.write("Case #" + str(z) + ": " + str(int((N-1)/2)+1) + " " + str(int((N-1)/2)) + "\n")
    else:
        outfile.write("Case #" + str(z) + ": " + str(int(N/2)) + " " + str(int(N/2)) + "\n")
outfile.close()
infile.close()
