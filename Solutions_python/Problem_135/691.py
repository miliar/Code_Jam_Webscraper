def magic_trick(filename):
    file = open(filename)
    out = open("output.txt", "w+")
    testcases = int(file.readline())
    for test in range(0, testcases):

##building the game
        ans = 0
        ans1 = 0
        ans2 = 0
        count = 0
        array1 = []
        array2 = []
        ans1 = int(file.readline())
        
        for i in range(0, 4):
            array1.append(file.readline().split(' '))
##        print(ans1)
##        print(array1)
        ans2 = int(file.readline())
        for i in range(0, 4):
            array2.append(file.readline().split(' '))
##        print(ans2)
##        print(array2)
        for i in range(0, 4):
            for j in range(0, 4):
                array1[i][j] = int(array1[i][j])
                array2[i][j] = int(array2[i][j])

##finding the answer
        for i in array1[ans1-1]:
            if i in array2[ans2-1]:
                ans = i
                count += 1
##                print(str(ans) + "\t" + str(count))
        
##outputting the answer
        if ans == 0:
            result = "Volunteer cheated!"
        elif count == 1:
            result = ans
        elif count > 1:
            result = "Bad magician!"
        final = ("Case #" + str(test+1) + ": " + str(result) + "\n")
##        print(final)
        out.write(final)

    file.close()
    out.close()
