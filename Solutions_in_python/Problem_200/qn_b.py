
def tidy(a):
    data = list(a)
    for i in range(len(data)-1):
        if data[i]>data[i+1]:
            return False
    return True

try:
    infile = open("B-small-attempt0.in","r")
    infile.readline()
    data = infile.readlines()
    infile.close()
    outfile = open("answer_b_small.txt","w")
    case = 0
    for line in data:
        case +=1
        number = int(line.rstrip())
        while True:
            if tidy(str(number)) == True or number < 10:
                y = number
                break
            else:
                number -= 1
                
                
        outfile.write("Case #")
        outfile.write(str(case))
        outfile.write(": ")
        outfile.write(str(y))
        outfile.write("\n")
    outfile.close()

    print("Done")

except IOError:
    print("IOError")
