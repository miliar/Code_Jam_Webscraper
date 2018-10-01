input_file = "largein1.in"

f = open(input_file)

def nextLine():
    line = f.readline()
    if (line.endswith("\n")):
        return line[0:-1]
    else:
        return line;

def greaterThan(num1, num2):
    x = (num1 - num2)
    if (x > 0):
        if  (x > 1*10**(-4)):
            return True
        else:
            return False
    else:
        return False


num_cases = int(nextLine())

length = [0] * num_cases
vector_1 = [0] * num_cases
vector_2 = [0] * num_cases

for case in range(num_cases):
    length[case] = nextLine()
    vector_1[case] = nextLine().split(" ")
    vector_2[case] = nextLine().split(" ")
    
##########Process INFO###########
    
for case in range(num_cases):
    lowest = 0

    vector_1[case].sort()
    vector_2[case].sort(reverse=True)

    temp = vector_2[case]

    arr = [0]* int(length[case])

    for i in range(int(length[case])):
        low = int(temp[0])
        for i2 in range(len(temp)):
            if int(temp[i2]) > low:
                low = int(temp[i2])
        temp.remove(str(low))
        arr[i] = low

    vector_2[case] = arr

    temp = vector_1[case]

    arr = [0]* int(length[case])

    for i in range(int(length[case])):
        low = int(temp[0])
        for i2 in range(len(temp)):
            if int(temp[i2]) < low:
                low = int(temp[i2])
        temp.remove(str(low))
        arr[i] = low

    vector_1[case] = arr

##    print vector_1[case]
##    print vector_2[case]
##    
    for i in range(int(length[case])):
        lowest = lowest + int(vector_1[case][i]) * int(vector_2[case][i])


    print "Case #" + str(case + 1) + ": " + str(lowest)
