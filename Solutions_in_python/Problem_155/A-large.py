input_file = iter(open('A-large.in').read().splitlines())

for test_case in range(int(next(input_file))):
    max_shyness, number_shyness = next(input_file).split()
    max_shyness = int(max_shyness)
    count = 0
    people = 0
    if max_shyness > 0:
        for i in range(1, max_shyness + 1):
            people += int(number_shyness[i - 1])
            if people < i and int(number_shyness[i]) > 0:
                addition = i - people
                count += addition
                people += addition
    print ('Case #', test_case + 1, ': ', count, sep = '')
