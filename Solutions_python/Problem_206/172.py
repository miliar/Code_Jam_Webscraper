from math import ceil

#FILE_PATH = "example.txt"
#OUTPUT_FILE_PATH = 'example.out'

#FILE_PATH = "A-small-attempt0.in"
#OUTPUT_FILE_PATH = 'A-small-attempt0.out'

FILE_PATH = "A-large.in"
OUTPUT_FILE_PATH = 'A-large.out'

def read_file(path):
    test_cases = []
    with open(path, 'rb') as f:
        lines = f.readlines()
        i = 1
        while i < len(lines):
            first_line = lines[i]
            if first_line.endswith('\n'):
                lines[i] = first_line[:-1]
            sp = first_line.split(' ', 1)
            D, N = int(sp[0]), int(sp[1])
            horses = []
            first_idx = i
            while i < first_idx + N:
                i += 1
                if lines[i].endswith('\n'):
                    lines[i] = lines[i][:-1]
                sp = lines[i].split(' ', 1)
                horses.append((int(sp[0]), int(sp[1])))
            test_cases.append((D, N, horses))
            i += 1
    print test_cases
    return test_cases

def output_solution(solution, path):
    lines = []
    with open(path, 'wb') as f:
        for (i, sol) in enumerate(solution):
            lines += ['Case #{index}: {solution}\n'.format(index=i+1, solution=sol)]
        f.writelines(lines)
    
# The only interesting function in this file
def solve_test_case(test_case):
    D, N, horses = test_case[0], test_case[1], test_case[2]
    max_time = 0.0
    for horse in horses:
        horse_time = (D - horse[0]) / float(horse[1])
        max_time = max(max_time, horse_time)
    return D / max_time
    
if __name__ == "__main__":
    test_cases = read_file(FILE_PATH)
    solution = [solve_test_case(test_case) for test_case in test_cases]
    print solution
    output_solution(solution, OUTPUT_FILE_PATH)