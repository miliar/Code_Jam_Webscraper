def main():
    
    file = open("A-large.in", "r")
    out  = open("answer1.txt", "w")
    cases = int(file.readline().rstrip())
    first = True
    for case in range(cases):
        #print("Case: " + str(case+1))
        newline = ""
        line = file.readline().rstrip().split(" ")
        #print(line)
        maxShy = int(line[0])
        distrib = line[1]
        peopleLeft = int(distrib[0])
        friends = 0
        if peopleLeft == 0:
            friends += 1
            peopleLeft += 1
        for i in range(1, len(distrib)):
            #print("People Left: " + str(peopleLeft))
            #print(distrib[i])
            peopleLeft -= 1
            peopleLeft += int(distrib[i])
            if peopleLeft == 0:
                #print("Added friend!")
                friends += 1
                peopleLeft += 1
            

        answer = friends
        
        if(first):
            first = not first
        else:
            newline = "\n"

        out.write(newline + "Case #" + str(case+1) + ": " + str(answer))
    
main()
