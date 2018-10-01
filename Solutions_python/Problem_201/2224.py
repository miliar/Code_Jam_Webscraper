import sys
import math

def reading_the_file(input_file):
    f = open(input_file, 'r+')
    return f

def getting_test_cases(f):
    y0 = []
    for counter, line in enumerate(f):
        case = counter + 1
        if counter == 0:
            number_of_test_cases = line
            continue
        if counter > 0:
            y0.append(line[:-1])
    return {'C':[x for x in y0], 'cases' : int(number_of_test_cases) }

def going_through_the_cases(C,cases):
    output_file_name = sys.argv[1][:-2]+'out'
    with open(output_file_name, 'w') as f:
        for i in range(cases):
            result = algorithm(C[i])
            f.write('Case #{}'.format(i+1)+': '+ result)

def algorithm(C):
    List = C.split(' ')
    N = int(List[0])
    K = int(List[1])
    Is_plus_one = 0
    Level = int(math.ceil(math.log((K+1),2)))
    if 2**Level >= N:
        [max, min] = [0,0]
    Num_of_places = (N - (2**Level) + 1)
    Num_of_plus_ones = Num_of_places%(2**(Level-1))
    People_for_further_spaces = K - 2**(Level - 1) + 1
    [max_val, min_val] = [int(math.ceil(Num_of_places/(2**(Level-1))/2.0)), int(math.floor(Num_of_places/(2.0**(Level-1))/2))]
    if Num_of_plus_ones >= People_for_further_spaces:
        if max_val == min_val:
            max_val += 1
        else:
            min_val += 1
    Place = str(max_val)+' '+str(min_val)+'\n'
    return Place


def main():
    input_file = sys.argv[1]
    going_through_the_cases(**getting_test_cases(reading_the_file(input_file)))

if __name__ == '__main__':
    main()

