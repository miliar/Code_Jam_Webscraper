#import numpy as np

def read_file():
    '''
    Reads the input file
    '''
    n_data = int(raw_input())  # read a line with a single integer
    numbers =[]
    for i in range(n_data):
        numbers.append(int(raw_input()))
        #print numbers[i]

    return numbers

def solve_problem(data):
    for i in range(len(data)):
        ni = data[i]
        char = "{}".format(ni)
        while True:
            correct = False
            newchar = char
            for j in range(1, len(char)):
                if correct:
                    newchar += '9'
                else:
                    if char[j] == '0':
                        val = int(char[0:j])-1
                        newchar = "{}".format(val)
                        newchar += '9'
                        correct = True
            ni = int(newchar)
            char = "{}".format(ni)

            end = True
            for j in range(len(char)-1):
                if char[-(1+j)] < char[-(2+j)]:
                    end = False
                    ni -= 1
                    char = "{}".format(ni)

            if end:
                break


        line = "Case #{}: {}".format(i+1, ni)
        print(line)

if __name__ == '__main__':
    #filename = sys.argv[1]
    #print filename
    # read
    data = read_file()
    #print len(data.keys())
    #print len(flip_sizes)

    # solve
    #print "Solving"
    solve_problem(data)

    # write
    #outfile = filename.split('.')[0]
    #outfile += ".out"
    #print outfile
    #write_file(result)
