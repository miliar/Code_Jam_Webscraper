import sys
import random


#111111111111111110

def open_file(file_name, mode):
    try:
        the_file = open(file_name, mode)
    except IOError as e:
        print("Unable to open the file", file_name, "Ending program.\n", e)
        input("\n\nPress the enter key to exit.")
        sys.exit()
    else:
        return the_file

def next_line(the_file):
    line = the_file.readline()
    line = line.replace("\n", "")
    return line


file = open("B-small-attempt0.in")
Count = int(next_line(file))
StrA = []

i = 0
while i <= Count-1:
    N = int(next_line(file))
    j = N
    while j >= 1:
        k = str(j)

        Tidy = 1
        a = 0
        while a <= len(k)-2:
            b = int(k[a])
            c = int(k[a+1])
            if b > c:
                Tidy *= 0
            else:
                Tidy *= 1
            a += 1

        if Tidy == 1:
            StrA.append(k)
            j = 0
        else:
            j -= 1
    i += 1
file.close()


file = open_file("B output-small.in", "a")
i = 0
while i <= Count-1:
    file.write("Case #" + str(i+1) + ": " + StrA[i] + "\n")
    i += 1
file.close()
