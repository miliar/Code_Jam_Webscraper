
def isPalin(num):
    check = list(num)
    size = len(check)
    if size > 1:
        fhalf = ""
        shalf = ""
        for i in range(size/2):
            fhalf += check[i]
            shalf += check[size - i - 1]
        #print fhalf, shalf
        if shalf == fhalf:
            #print fhalf, shalf
            return True
    elif size == 1:
        return True
    else:
        return False
        



infile = open("C-small-attempt1.in", "r")
outfile = open("outputc.txt", "w")

num_T = int(infile.readline().strip())
count = 0

while count < num_T:
    count += 1
    bot, top = [int(x) for x in infile.readline().strip().split()]
    fair_count = 0
    for i in range(0, top/2 + 2):
        root = str(i)
        #print root
        if isPalin(root):
            sqre = i ** 2
            if sqre <= top and sqre >= bot:
                #print sqre
                if isPalin(str(sqre)):
                    fair_count += 1
                    print sqre
    message = "Case #%d: %d" % (count, fair_count)
    print message
    outfile.write(message + "\n")

