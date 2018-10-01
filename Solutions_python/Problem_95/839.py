#googlerese


#Opening input file:

while True:
    choice = input("Large or Small set: ")
    if choice == "s":
        file = open("G:\Downloads\chrome download\B-small-practice.in")
        fname = "B-small-practice.in"
        break
    elif choice == "l":
        file = open("G:\Downloads\chrome download\B-large-practice.in")
        fname = "B-large-practice.in"
        break
    elif choice == "t":
        file = open("G:\\Downloads\\chrome download\\test.txt")
        fname = "test.txt"
        break
    elif choice == "c":
        fname = input('Enter file name: ')
        floc = "G:\Downloads\chrome download\\" + fname
        file = open(floc)
        break
    else:
        print("Wrong Choice")

flist = file.readlines()
flist = [temp.strip() for temp in flist]
import pickle
nfile = open("G:\codejam\\key.txt", "rb")
key = pickle.load(nfile)
key[" "] = " "

strings = []
final = []
tempstr = ''

#Do the work here:

for i in range(1,len(flist)):
    strings.append("".join(flist[i]))
    
for temp in strings:
    for char in temp:
        tempstr += key[char]
    final.append(tempstr)
    tempstr = ''
    


#Writing to Output file:
    
wfile = open("G:\codejam\\" + fname, "w")

for i in range(int(flist[0])):
    wfile.write("Case #" + str(i+1) + ": " + final[i] + "\n")

wfile.close()
             
