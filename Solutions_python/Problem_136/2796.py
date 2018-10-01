from optparse import OptionParser



def solve_B(C, F, X):
    nb_cookies = 0
    prod = 2
    time = 0
    while nb_cookies < X:
        # make a choice
        tprod_no_fact = X / prod
        tprod_1fact = X / (prod + F) + (C / prod)
        if tprod_no_fact <= tprod_1fact:
            nb_cookies = X
            time += X / prod      
        else:
            time += C / prod
            nb_cookies = 0
            prod += F
    return time

def problem_B(filename):
    with open(filename, 'r') as fin:
        lines = [l.rstrip("\n") for l in fin.readlines()]
    ntestcases = int(lines[0])
    for i in range(ntestcases):
        C, F, X = [float(s) for s in lines[i + 1].split(" ")]
        print "Case #%d: %s" % (i+1, solve_B(C, F, X))





if __name__ == "__main__":
    parser = OptionParser()
    (options, args) = parser.parse_args()

    if len(args) != 1:
        parser.error("incorrect number of arguments")
    problem_B(args[0])
