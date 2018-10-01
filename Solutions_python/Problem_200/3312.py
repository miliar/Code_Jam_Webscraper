def main():
    fileName = "B-large.in"
    file = open(fileName)

    # Loop for the number of tests there are.
    for case in range(1, int(file.readline()) + 1):
        # Read in the last largest number.
        ceiling = file.readline()
        digits = [int(i) for i in list(ceiling.strip())]

        # Iterate through the digits.
        currentIndex = 0
        while (True):
            if len(digits) == currentIndex + 1:                    
                print("Case #" + str(case) + ": " + str(int(''.join([str(i) for i in digits]))))
                break

            if digits[currentIndex] <= digits[currentIndex + 1]:
                currentIndex += 1
            else:
                while(digits[currentIndex] == 0):
                    currentIndex -= 1

                digits[currentIndex] -= 1
                for index in range(currentIndex + 1, len(digits)):
                    digits[index] = 9;
                currentIndex = max(currentIndex - 1, 0)

if __name__ == "__main__":
    main()
