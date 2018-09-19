infile = open("GCJ1.txt")
line = infile.readlines()
x = []
for i in line:
    x.append(i.split())
infile.close()

count = 1
t = int(line[0].split()[0])
i = 0
while i != t:
    j = count
    find = j + int(x[j][0])
    first = x[find]
    j += 5
    find = j + int(x[j][0])
    second = x[find]

    number = []
    for k in first:
        for l in second:
            if k == l:
                number.append(k)

    outfile = open("GCJ2.txt", 'a')

    if len(number) == 1:
        outfile.write("Case #" + str(i+1) + ': ' + str(number[0]))
    elif len(number) > 1:
        outfile.write(("Case #" + str(i+1) + ': '  + "Bad magician!"))
    else:
        outfile.write(("Case #" + str(i+1) + ': '  + "Volunteer cheated!"))
    outfile.write('\n')
    outfile.close()




    
    count += 10
    i += 1
    
