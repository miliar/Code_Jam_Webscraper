from optparse import OptionParser
import string

def solve(N,Vines,D):
    Position = 0
    NextVine = 0
    Cache = {}
    return can_reach_target(Position, NextVine, Vines, N, D, Cache) and "YES" or "NO"

def can_reach_target(Position, NextVine, Vines, N, D, Cache):
    # Only check this case once.
    if Cache.get((Position, NextVine), False):
        return False
    Cache[(Position,NextVine)] = True
    Max_Dist = Position - Vines[NextVine][0]
    Position = Vines[NextVine][0]
    if Max_Dist < 0:
        Max_Dist *= -1
    if Max_Dist > Vines[NextVine][1]:
        Max_Dist = Vines[NextVine][1]
    if Position + Max_Dist >= D:
        return True
    # Try swinging forwards first
    TempNextVine = NextVine + 1
    while TempNextVine < N and Vines[TempNextVine][0] - Position <= Max_Dist:
        if can_reach_target(Position,TempNextVine,Vines,N,D,Cache):
            return True
        TempNextVine += 1
    # Then see if back helps.
    TempNextVine = NextVine - 1
    while TempNextVine > -1 and Position - Vines[TempNextVine][0] <= Max_Dist:
        if can_reach_target(Position,TempNextVine,Vines,N,D,Cache):
            return True
        TempNextVine -= 1
    return False


def parse_case(input_file):
    N = int(input_file.readline())
    Vines = []
    for i in range(N):
        data_line = input_file.readline()
        bits = data_line.split()
        Vd = int(bits[0])
        Vl = int(bits[1])
        Vines.append((Vd, Vl))
    D = int(input_file.readline())
    return N, Vines, D

def main():
    import sys
    sys.setrecursionlimit(1000000000)
    parser = OptionParser()
    parser.add_option("-f", "--file", dest="filename",
                      help="read input from FILE", metavar="FILE")

    (options, args) = parser.parse_args()
    if not options.filename:
        parser.error("Must provide a filename.")
    input_file = open(options.filename, "r")
    total_cases = int(input_file.readline())
    case_number = 0
    while case_number < total_cases:
        case_number += 1
        data_args = parse_case(input_file)
        print "Case #%d: %s" % (case_number, solve(*data_args))

if __name__ == "__main__":
    main()