no_of_cases = 0
case_lines = []
with open("output.txt", "r") as my_file:
    no_of_cases = my_file.readline()
    for i in range(0, int(no_of_cases)):
        case_lines.append(my_file.readline().strip("\n"))
for i in range(0, len(case_lines)):
    a = case_lines[i].split(" ")
    shyness_str = a[1]
    len_shyness_str = len(a[1])
    f = 0
    for j in range(0, len_shyness_str):
        s = 0
        for k in range(0, j):
            s += int(shyness_str[k])
        if (s + f) < j:
            f += j - (s + f)
    
    print "Case #" +str(int(i + 1))+ ": " + str(f)
