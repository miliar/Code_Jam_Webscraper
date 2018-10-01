def read_tc(fl):
    #ingnore the fact that the input could be wrong
    case_set = []
    for i in range(2):
        card_arrangement = []
        card_in_line = int(fl.readline())
        for ii in range(4):
            card_arrangement.append(fl.readline().split())
        case_set.append((card_in_line, card_arrangement))
    return case_set

def read_input(fl):
    tc_list = []
    in_str = fl.readline()
    if not in_str:
        print "Bad input"
        return None
    tc_count = 0
    try:
        tc_count = int(in_str)
    except ValueError:
        print "Bad input"
        return None
    indx = 0
    while indx < tc_count and in_str:
        tc = read_tc(fl)
        tc_list.append(tc)
        indx += 1
    return tc_list

def solve_the_problem(my_input):
    case_num = 1
    for item in my_input:
        line1 = item[0][1][item[0][0]-1]
        line2 = item[1][1][item[1][0]-1]
        intersection = [val for val in line1 if val in line2]
        if len(intersection) == 1:
            print "Case #%d: %d" % (case_num, int(intersection[0]))
        elif len(intersection) > 0:
            print "Case #%d: Bad magician!" % case_num
        else:
            print "Case #%d: Volunteer cheated!" % case_num
        case_num += 1

if __name__ == "__main__":
    with open('/Users/knazaren/Downloads/A-small-attempt1.in', 'r') as f:
        inpt = read_input(f)
        solve_the_problem(inpt)

