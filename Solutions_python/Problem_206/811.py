import sys


def load_info(f):
    line = f.readline()
    out = int(line)
    return out    

def my_function(f, case_num):
    print_info = []
    line = f.readline().strip('\n').split(' ')
    D, N = [int(x) for x in line]
    travelling_time = 0
    for horse in xrange(N):
        line = f.readline().strip('\n').split(' ')
        k_i,s_i = [int(x) for x in line]
        tt_i = 1.0 * (D - k_i)/s_i
        if tt_i > travelling_time:
            travelling_time = tt_i
    res = D/travelling_time
        
    print_info.append('Case #' + str(case_num+1) + ': ' + '%.6f' % res)
    print_info.append('\n')

    return print_info
    
if __name__ == '__main__':
    while True:
        print('\n---------------------------')
        print("Type in the input and output files' names separated by a white space, or 'exit' when you're done, thx. ")
        
        sys.stdout.write('2017 R1B_1 > ')
        input_args = str(raw_input())
        try:
            if input_args == 'exit':
                break
            elif input_args == '':
                continue
            else:
                args = input_args.split(' ')
                input_file = args[0]
                output_file = args[1]
        except:
            print('Invalid input. Please try again.')
        else:
            f_in = open(input_file)
            f_out = open(output_file, 'w')
            
            num_of_tests = load_info(f_in)
            try:
                for x in xrange(num_of_tests):
                    f_out.writelines(my_function(f_in, x))
##            except:
##                print('something wrong')
##            else:
##                print('File is built successfully!!!!')
##                print('---------------------------\n')
            finally: 
                f_in.close()
                f_out.close()
