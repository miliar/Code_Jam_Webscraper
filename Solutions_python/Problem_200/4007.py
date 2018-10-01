def main():
    number_of_inputs = int(input())

    for currentInput in range(1, number_of_inputs + 1):
        searching = True
        current_number = input()
        current_number_list = [int(digit) for digit in current_number]

        while searching:

            if sorted(current_number_list) == current_number_list:
                searching = False

            else:
                current_number = str(int(current_number) - 1)
                current_number_list = [int(digit) for digit in current_number]

        print("Case #%d: %s" % (currentInput, current_number))


if __name__ == "__main__":
    main()
