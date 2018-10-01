import sys

def main():
    # Open the file
    if(len(sys.argv) < 2):
        print("Not enough arguments. Exiting.")
        exit()
    file = open(sys.argv[1], 'r')

    # Read the first line of the file, getting test cases
    totalCases = int(file.readline().strip())
    testCases = 0

    # Get first line of input, loop until no more lines are found
    line = file.readline().strip()
    while(line != ""):
        testCases += 1

        dest, horses = [int(i) for i in line.split(' ')]

        time = 0.000000000000000000000001

        # Loop through the char in the line read
        for i in range(0, horses):
            horse = [int(j) for j in file.readline().strip().split(' ')]

            if(((dest - horse[0]) / horse[1]) > time):
                time = (dest - horse[0]) / horse[1]

        # Print the output in correct formatting
        print("Case #" + str(testCases) + ": " + str(dest / float(time)))
        line = file.readline().strip()

    file.close()

if(__name__ == "__main__"):
    main()
