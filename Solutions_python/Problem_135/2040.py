def solve(n1, n2, arrange1, arrange2):
    global wfile
    global case

    numIn = 0
    lastNum = -1
    for card1 in arrange1[n1-1]:
        for card2 in arrange2[n2-1]:
            if card1 == card2:
                numIn += 1
                lastNum = card1

    print(str(lastNum) + " " + str(numIn))

    ans = ""
    if numIn > 1:
        ans = "Bad magician!"
    elif numIn == 1:
        ans = lastNum
    else:
        ans = "Volunteer cheated!"

    wfile.write("Case #{0}: {1}\n".format(case, ans))
    case += 1


f = open("input.in")
f.readline()

wfile = open("output.out", "w")

n1 = -1
n2 = -1
arrange1 = []
arrange2 = []

case = 1

line = f.readline()
while line != "":
    n1 = int(line)
    for i in range(4):
        arrange1.append(f.readline().split())
    n2 = int(f.readline())
    for i in range(4):
        arrange2.append(f.readline().split())
            
    solve(n1, n2, arrange1, arrange2)
    n1 = -1
    n2 = -2
    arrange1 = []
    arrange2 = []
    
    line = f.readline()
