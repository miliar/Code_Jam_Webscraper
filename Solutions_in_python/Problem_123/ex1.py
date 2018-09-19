
class Problem(object):
    def __init__(self, A, N, values):
        self.A = A
        self.N = N
        self.values = values
        self.values.sort()

def tryit(problem, mote, index, max_count):
    if (index == problem.N):
        return 0
    if (max_count < 0):
        return 10000
    if (problem.values[index] < mote):
        return tryit(problem, mote + problem.values[index], index + 1, max_count)
    else:
        a = tryit(problem, mote * 2 - 1, index, max_count - 1) + 1 #added a mote
        b = tryit(problem, mote, index + 1, max_count - 1) + 1     #removed mote
        return min(a, b)

def getSolution(problem):
    op_count = tryit(problem, problem.A, 0, problem.N)
    return str(op_count)

def readProblem(input_file):
    A, N = [int(x) for x in input_file.readline().split(" ")]
    values = [int(x) for x in input_file.readline().split(" ")]
    return Problem(A, N, values)

def executeFile(file_path):
    input_file = file(file_path, "r")
    output_file = file(file_path + ".out", "w")
    count = int(input_file.readline());
    index = 0
    while (index < count):
        problem = readProblem(input_file)
        sol = getSolution(problem)
        output_file.write("Case #" + str(index + 1) + ": " + sol + "\n")
        index = index + 1
    output_file.close()

def main():
    import sys
    if (len(sys.argv) < 2):
        print "Wrong number of arguments!\n" + \
              "Arguments: file_path"
        return
    for i in xrange(len(sys.argv) - 1):
        executeFile(sys.argv[i + 1])
    
if (__name__ == "__main__"):
    main()
