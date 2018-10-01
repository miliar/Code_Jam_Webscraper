def CheckTidyNess(number):
    #list = []
    max = 0
    for d in number:
        #list.extend(d)
        if int(d) < max:
           return False
        max = int(d)
    return True

def FindNearTidyNumber(n, case):
    for i in range(n,0,-1):
        #print("Checking: " + str(i))
        if CheckTidyNess(str(i)):
            print(i)
            f2.write("Case #" + str(case) + ": " + str(i) + '\n')
            break

def TidyUpBam(number):
    #nope...
    list = []
    for i in range(0,len(number)-1,1):
        n1 = int(number[i+1])
        n2 = int(number[i])
        if n1 < n2:
            list.append(n2-1)
            for j in range(i+1,len(number),1):
                list.append(9)
            break
        else:
            list.append(n2)
    print(list)

filename = "C:\\Users\\duckarcher\\Downloads\\B-small-attempt1.in"
f = open(filename)
f2 = open(filename.replace(".in", ".out"), 'w')
case = 1
next(f)
for line in f:
    line = line.strip('\n')
    print("[+] Trying number '" + line + "'")
    #test = CheckTidyNess(line)
    #print(test)
    FindNearTidyNumber(int(line), case)
    case += 1
    '''if not CheckTidyNess(line):
        TidyUpBam(line)
    else:
        print(line)'''