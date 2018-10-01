with open("clap_in.txt") as f:
    number_cases = int(f.readline().strip())

    #for line in f:
    for case in range(1, number_cases+1):
        
        data = f.readline().split()

        addFriends = 0;
        numStanding = 0;

        for shyness in range(0, int(data[0])+1):
            if numStanding >= shyness:
                #this many more people are now standing
                numStanding = numStanding + int(data[1][shyness])
            else:
                #numstanding is less than shyness.
                #add more standing people
                #+the difference between numstanding and shyness
                addFriends = addFriends + (shyness-numStanding)
                numStanding = numStanding + int(data[1][shyness]) + (shyness-numStanding)

        print("Case #" + str(case) + ": " + str(addFriends))
