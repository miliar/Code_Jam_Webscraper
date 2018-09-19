input_file = open("A-large.in.txt")
output_file = open("output.txt", "w")
T = int(input_file.readline().strip())
for case in range(T):
    output_file.write("Case #" + str(case+1) + ": ")
    string = input_file.readline().strip()
    str_len = len(string)
    key = []
    for char in string:
        if char not in key:
            key.append(char)
    base = len(key)
    if base == 1:
        base = 2
    total = 0
    for x in range(str_len):
        val = key.index(string[x])
        if val == 0:
            val = 1
        elif val == 1:
            val = 0
        total += int(val)*base**(str_len-x-1)
    output_file.write(str(total) + "\n")
output_file.close()
