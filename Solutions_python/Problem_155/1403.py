# Hello World program in Python
    
infile = open("A-small-attempt1.in", "r")

lines = infile.readlines()

count = 0

for line in lines:
    count += 1
    if count == 1:
        pass
    elif count > 1:
        max_s = int(line[0])
        line_length = max_s + 3
        audience = line[2:line_length]
        audience_count = 0
        friends = 0
        for i in range(2,line_length):
            if line[i] == "0":
                pass
            elif audience_count >= (i-2):
                audience_count += int(line[i])
            else:
                friends += i - 2 - audience_count
                audience_count += (i-2-audience_count) + int(line[i])
        outfile = open("output.txt", "a")
        outfile.write("Case #" + str(count-1) + ": " + str(friends) + "\n")

outfile.close()
