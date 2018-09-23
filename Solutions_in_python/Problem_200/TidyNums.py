test_cases = input().strip()
for i in range(int(test_cases)):
    number = int(input().strip())
    tidy = False
    while not tidy:
        tidy = True
        for j in range(len(str(number))-1, 0, -1):
            if(int(str(number)[j]) < int(str(number)[j-1])):
                tidy = False
        if tidy:
            print("Case #" + str(i+1) + ": " + str(number))
        else:
            number-=1

                

