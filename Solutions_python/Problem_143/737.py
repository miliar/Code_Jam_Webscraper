def main():
    fileName = "B-small-attempt0.in"
    file = open(fileName)

    # Loop for the number of tests there are.
    for case in range(1, int(file.readline()) + 1):
        # Read in the values.
        line = file.readline().split()
        a = int(line[0])
        b = int(line[1])
        k = int(line[2])

        # Compare the two numbers together.
        count = 0
        for currentA in range(a):
            for currentB in range(b):
                if currentA & currentB < k:
                    count += 1
        print("Case #" + str(case) + ": " + str(count))
        
if __name__ == "__main__":
    main()
