import sys


def main(input_data):
    no_of_inputs = int(input_data.readline())
    output_file = open('/home/ubuntu/output.txt', 'w')
    try:
        for count in range(0, no_of_inputs):
            friends_needed = 0
            total_no_of_people = 0
            test_input = input_data.readline().split(" ")
            max_shyness = int(test_input[0])
            shyness_values = test_input[1]
            for index in range(0, max_shyness + 1):
                no_of_people = int(shyness_values[index])
                if index > total_no_of_people and no_of_people > 0:
                    friends_needed += index - total_no_of_people
                    total_no_of_people += index - total_no_of_people
                total_no_of_people += no_of_people

            output_file.write("Case #" + str(count+1) + ": " + str(friends_needed) + "\n")

    finally:
        input_data.close()
        output_file.close()


if __name__ == '__main__':
    if len(sys.argv) < 2:
        raise Exception("Give name of input file as parameter.")
    else:
        input_data = open(sys.argv[1], 'r')
        main(input_data)
