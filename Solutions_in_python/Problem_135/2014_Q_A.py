import ProblemFileIO

def main():
    filename = 'A-small-attempt0'
    ProblemIO = ProblemFileIO.ProblemFileIO(filename, case_function)
    for (first_row, second_row) in ProblemIO.case_generator():
        result = solve(first_row, second_row)
        ProblemIO.write_result(result)

def case_function(file_object):
    first_row_num = ProblemFileIO.read_int(file_object)
    for i in xrange(4):
        read_row = ProblemFileIO.read_int_list(file_object, ' ')
        if (first_row_num == i + 1):
            first_row = read_row
    second_row_num = ProblemFileIO.read_int(file_object)
    for i in xrange(4):
        read_row = ProblemFileIO.read_int_list(file_object, ' ')
        if (second_row_num == i + 1):
            second_row = read_row
    return (first_row, second_row)
            
def solve(first_row, second_row):
    first_set = set(first_row)
    second_set = set(second_row)
    intersection_set = first_set.intersection(second_set)
    if (0 == len(intersection_set)):
        result = 'Volunteer cheated!'
    if (1 == len(intersection_set)):
        result = list(intersection_set)
        result = str(result[0])
    if (2 <= len(intersection_set)):
        result = 'Bad magician!'
    return result
    
if __name__ == '__main__':
    main()