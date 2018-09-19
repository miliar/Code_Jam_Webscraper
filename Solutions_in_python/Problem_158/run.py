import sys
import time
from decimal import *

def open_io_files():
    assert len(sys.argv) > 1, "Error: missing input file name argument."

    try:
        input_filename = sys.argv[1]
        file_in = open(input_filename, "r")
        print "Opening file \"%s\" in read." %  input_filename
    except:
        assert False, "Error, could not read file \"%s\"." % input_filename

    if len(sys.argv) > 2:
        try:
            output_filename = sys.argv[2]
            file_out = open(output_filename, "w")
            print "Opening file \"%s\" in write." % output_filename
        except:
            assert False, "Error: could not write file \"%s\"." % output_filename
    else:
        print "Warning: no output file given as argument."
        file_out = None

    return file_in, file_out

def quick_winner(X, R, C):
    area = R * C
    mindim = min(R, C)
    maxdim = max(R, C)

    if (   area < X # Not enough space
        or area % X > 0 # Cannot fit in the grid because not modulo
        or X >= (mindim * 2 + 1) # Can always go outside of the area
        or X >= (mindim * 2) and X > 2 # Can always split in two blocks impossible to fill
        or X > maxdim
        or X >= 7
       ):
        return "RICHARD"

    if (   X <= 2 # Can always fit
        or maxdim == 3
       ):
        return "GABRIEL"

    return "GABRIEL"

def process_test(test_id):
    result = "Case #%d: " % test_id

    X, R, C = map(int, file_in.readline().split(" "))
    print "X=", X, "R=", R, "C=", C

    winner = quick_winner(X, R, C)
    if winner is None:
        TODO



    result = "{0}{1}".format(result, winner)

    return result

if __name__ == "__main__":
    start_time = time.time()

    print getcontext()

    # Open input and output files
    file_in, file_out = open_io_files()

    # Extract the number of tests
    T = int(file_in.readline())

    # Process every test and write to file
    for test_id in range(1, T+1):
        result = process_test(test_id)
        if file_out:
            file_out.write(result + "\n")
        else:
            print result

    time = time.time() - start_time
    print "%s executed in %g seconds." % (sys.argv[0], time)
