import copy
import pdb


def getInput(path):
    f = open(path)
    lines = f.readlines()
    f.close()
    return lines


def print_ouput():
    lines = getInput("inputA.txt")
    no_cases = int(lines[0].strip())
    case = 1
    while (case<=no_cases):
        s_max = int(lines[case].split()[0])
        shyness_list = [int(x) for x in lines[case].split()[1].strip()]
        sol = get_solution(shyness_list)
        print "Case #{0}: {1}".format(case, sol)
        case  += 1


def get_solution(shyness_list):
    modified = False
    no_of_ppl_added = 0
    modified_list = copy.deepcopy(shyness_list)
    while True:
        test = check_if_done(modified_list)
        if test["result"] is True:
            return no_of_ppl_added
        else:
            modified_list[0] = modified_list[0] + test["data"]["shortage"]
            modified= True
            no_of_ppl_added += test["data"]["shortage"]
    pdb.set_trace()
    print "No result found!"
    


def check_if_done(shyness_list):
    sum_list = []
    for index, val in enumerate(shyness_list):
        if index == 0:
            sum_list.append(0)
        else:
            sum_list.append(sum_list[index-1] + shyness_list[index-1])
    reversed_sum_list = [x for x in reversed(sum_list)]
    """
    for index, no_of_ppl in enumerate(reversed(shyness_list)):
        shyness_value = len(shyness_list) - 1 - index
        #ppl_already_standing = sum(shyness_list[0:-index-1])
        ppl_already_standing = reversed_sum_list[index]
        if shyness_value > ppl_already_standing:
            return {'result': False, 'data': {"shortage": shyness_value - ppl_already_standing, "": ""}}
    return {'result': True}
    """
    for index, no_of_ppl in enumerate(shyness_list):
        shyness_value = index
        ppl_already_standing = sum_list[index]
        if shyness_value > ppl_already_standing:
            return {'result': False, 'data': {"shortage": shyness_value - ppl_already_standing, "": ""}}
    return {'result': True}




print_ouput()

