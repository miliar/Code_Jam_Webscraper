def test(number):
    check = True
    for j in range (len(number)-1):
            if number[j] > number[j+1]:
                check = False
    return check
i = 0
file = open("B-small-attempt0.in","r")
output = open("output_file.txt","w")
testnum = int(file.readline())
for line in file:
    number = line.strip()
    while test(number) != True:
        number = str(int(number) - 1)
    i+=1
    output.write("Case #"+str(i)+": " + str(number)+"\n")
file.close()
output.close()
