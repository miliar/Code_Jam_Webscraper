import ProblemFileIO

def main():
    filename = 'B-small-attempt0'
    ProblemIO = ProblemFileIO.ProblemFileIO(filename, case_function)
    for (C, F, X) in ProblemIO.case_generator():
        result = solve(C, F, X)
        ProblemIO.write_result(result)

def case_function(file_object):
    return ProblemFileIO.read_float_list(file_object, ' ')
            
def solve(C, F, X):
    rate = 2
    done = False
    accumulated_time = 0
    upgrade_counter = 0
    while not done:
        time_no_upgrade = X/rate
        time_with_upgrade = C/rate + X/(rate + F)
        upgrade = time_with_upgrade < time_no_upgrade
        if upgrade:
            accumulated_time += C/rate
            rate += F
            upgrade_counter += 1
        else:
            accumulated_time += X/rate
            done = True
    print 'upgraded %d times' %upgrade_counter
    return '%.7f' % accumulated_time
    
if __name__ == '__main__':
    main()