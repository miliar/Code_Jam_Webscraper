fin = open("dance.txt")
fin = fin.readlines()

inputs = int(fin[0])
fin.pop(0)

case_num = 1

for case in fin:
    case = case.split(' ')

    googlers = int(case[0])
    case.pop(0)
    surprises_left = int(case[0])
    case.pop(0)
    desired_result = int(case[0])
    case.pop(0)

    good_results = 0

    for i in xrange(googlers):
        case[i] = int(case[i])
        modulus = case[i] % 3
        if case[i] == 0:
            if 0 == desired_result:
                good_results += 1
        elif modulus == 0:
            if case[i]/3 >= desired_result:
                good_results += 1
            elif case[i]/3 + 1 >= desired_result and surprises_left > 0:
                surprises_left -= 1
                good_results += 1
        elif modulus == 1:
            if case[i]/3 + 1 >= desired_result:
                good_results += 1
        elif modulus == 2:
            if case[i]/3 + 1 >= desired_result:
                good_results += 1
            elif case[i]/3 + 2 >= desired_result and surprises_left > 0:
                surprises_left -= 1
                good_results += 1

    print ("Case #%d: " % case_num) + str(good_results)

    case_num += 1

