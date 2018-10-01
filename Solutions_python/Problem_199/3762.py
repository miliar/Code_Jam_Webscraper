file_name = "A-large.in"
with open(file_name) as file:
    input_data = file.read().split("\n")

output_data = ""

t = int(input_data[0])
for l in range(1,t+1):
    
    line = input_data[l]
    s, k = line.split(" ")
    s_bool = []
    for c in s:
        s_bool.append(c == "+")
    
    k = int(k)

    # TODO verify that number of False is a multiple of k?
    # is it always solvable if it is?

    i = 0
    m = 0
    success = False
    while not success:
        if not s_bool[i]:
            if k < 1:
                break # failure
            elif i > len(s) - k:
                break # failure
            #print(s_bool)
            # flip pancakes [i:i+k]
            for j in range(k):
                s_bool[i+j] = not s_bool[i+j]
            m += 1
        i += 1
        if i == len(s):
            success = True

    output_line = "Case #%d: " %l
    if success:
        output_line += str(m)
    else:
        output_line += "IMPOSSIBLE"

    output_data += output_line + "\n"
    print([output_line,s,k])

with open(file_name[:-3] + ".out", 'w') as file:
    file.write(output_data)
