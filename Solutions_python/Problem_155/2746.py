f_input = open(r"C:\Users\Arthur\Desktop\A-small-attempt0.in", "r")
f_output = open(r"C:\Users\Arthur\Desktop\output.txt", "w")

def getAnswer(line):
    n, S = line.split(' ')
    n = int(n)
    i = suma = count = 0
    while i < n and suma < n:
        suma += int(S[i])
        i += 1
        if (suma < i) :
            count += 1
            suma += 1
    return count


for i in range(int(f_input.readline())):
    f_output.write("Case #%d: %d\n" % (i + 1, getAnswer(f_input.readline())))

f_input.close()
f_output.close()
