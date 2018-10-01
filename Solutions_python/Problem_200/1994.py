def tidy_numbers(filename):
    txt_file = open(filename, 'r')
    txt_file_result = open('B-large-result.txt', 'w')
    testCasesAmount = int(txt_file.readline())

    for x in range(1, testCasesAmount + 1):
        actual_number = int(txt_file.readline().rstrip('\n'))
        result = solve(actual_number)

        txt_file_result.write('Case #' + str(x) + ': ' + str(result) + '\n')

    txt_file_result.close()
    txt_file.close()

def solve(actual_number):

    aux_tidy = 1

    number_as_string = str(actual_number)
    smallest_tidy = str(aux_tidy)*len(number_as_string)
    
    if (actual_number < int(smallest_tidy)):
        return int('9'*(len(number_as_string)-1))

    smallest_tidy = list(smallest_tidy)
    smallest_tidy_aux = smallest_tidy

    for i in range(0, len(number_as_string)):
        
        while (int(''.join(smallest_tidy_aux)) < actual_number):
            aux_tidy += 1
            smallest_tidy_aux = smallest_tidy[0:i] + list(str(aux_tidy)*(len(number_as_string) - i))

        if (int(''.join(smallest_tidy_aux)) == actual_number):
            return actual_number

        aux_tidy -= 1
        smallest_tidy_aux = smallest_tidy[0:i] + list(str(aux_tidy)*(len(number_as_string) - i))
        smallest_tidy = smallest_tidy_aux

    return ''.join(smallest_tidy)

tidy_numbers('B-large.in')