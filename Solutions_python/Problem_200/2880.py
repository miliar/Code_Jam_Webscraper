
def lastTidyNumber(number):

    num_list = [int(c) for c in number]
    idx = len(num_list) - 1
    lastIndex = len(num_list)
    while idx > 0:
        if num_list[idx - 1] > num_list[idx]:
            num_list[idx] = 9
            num_list[idx - 1] = num_list[idx - 1] - 1
            lastIndex = idx
        idx = idx - 1

    while lastIndex < len(num_list):
        num_list[lastIndex] = 9
        lastIndex = lastIndex + 1

    return int(''.join(str(c) for c in num_list))


def main(input_file, output_file):

    with open(input_file) as input:
        number_list = input.readlines()

    print "Got {0} input numbers".format(number_list[0])


    number_list.pop(0)

    with open (output_file, 'w') as output:
        for idx, val  in enumerate(number_list):
            val = val.strip()
            print "*" * 20
            print "number {}".format(val)
            res = lastTidyNumber(val)
            print "lastTidyNumber: ", res
            output.write("Case #{0}: {1}\n".format(idx + 1, res))
    return


if __name__ == "__main__":
    input_file = "B-large.in"
    output_file = "B-large.out"
    main(input_file, output_file)