# Theme Park - For Google Code Jam 2010
# by Jonathan Sorce

# Open the file
parkin = open("C-small.in", "r")
# Obtain the number of test cases
T = int(parkin.readline())

parkout = open("C-small.out", "w")
for i in range(T):
    # total money = 0
    money = 0
    # obtain the values from the first line
    values = parkin.readline().split(" ")
    R = int(values[0])
    k =  int(values[1])
    N = int(values[2])
    groups = parkin.readline().split(" ")
    # convert them to integers
    for j in range(len(groups)):
        groups[j] = int(groups[j])

    # the roller coaster runs R times...
    for j in range(R):
        # k should stay a constant, so capacity will serve as a variable
        # that can be modified
        capacity = k
        # create an empty list (this will be explained later)
        onlist = []
        while True:
            # a try statement in case of index errors
            try:
                # if the next group can fit on the roller coaster
                if groups[0] <= capacity:
                    # lower the capacity
                    capacity -= groups[0]
                    # up the money by 1 euro per person
                    money += groups[0]
                    # at this point, normally the first item would be
                    # deleted and added to the end of the list - however,
                    # this allows for errors to be made in terms of
                    # the total number of people being smaller than the capacity
                    # of the roller coaster. So instead, it will be deleted
                    # and added to onlist - the people on the roller coaster
                    onlist.append(groups[0])
                    del groups[0]
                else:
                    groups += onlist
                    break
            except:
                # the except will only be reached if groups becomes an empty
                # list - [], so:
                groups = onlist
                break
    parkout.write("Case #" + str(i + 1) + ": " + str(money) + "\n")

parkout.close()
parkin.close()
raw_input("Press enter to exit.")
