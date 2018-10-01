import sys

DEBUG = True

def solver(row1, arr1, row2, arr2):
    possible_nums = set(arr1[row1 - 1])
    debug(possible_nums)
    possible_nums &= set(arr2[row2 - 1])
    debug(possible_nums)
    if len(possible_nums) == 1:
        debug(possible_nums)
        return possible_nums.pop()
    elif len(possible_nums) > 1:
        return "Bad magician!"
    else:
        return "Volunteer cheated!"

def ssi(s, func=int):
    """
    space separated integers
    """
    return map(func, s.strip('\n').split())

def rl():
    return sys.stdin.readline()

def debug(*args):
    if args[-1] is not False and DEBUG:
        msg = " ".join([str(m) for m in args])
        sys.stderr.write(msg + '\n')

def main():
    # open input file
    # input_file = open('infile.txt')
    
    cases = int(rl())
    output = []
    # loop through cases passing input to solver
    for c in xrange(cases):
        debug('Case #%d' % (c+1))
        row1 = int(rl())
        arr1 = [ssi(rl()) for i in range(4)]
        row2 = int(rl())
        arr2 = [ssi(rl()) for i in range(4)]
        answer = solver(row1, arr1, row2, arr2)
        output.append('Case #%d: %s\n' % (c+1, answer))
    # open output file
    output_file = sys.stdout
    # write ouput to file
    output_file.writelines(output)
    output_file.flush()



if __name__=='__main__':
    main()
