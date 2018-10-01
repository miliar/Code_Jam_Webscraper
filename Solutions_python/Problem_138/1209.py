
file_name = "D-large.in"
out_file_name = "test_war.out"

out_file = open(out_file_name, 'w')

def deceitful(num_of_blocks, naomi, ken):
    counter = 0
    index = 0
    for k in ken:
        if naomi[index] > k:
            index += 1
            counter += 1
    return counter

def normal(num_of_blocks, naomi, ken):
    index = 0
    counter = 0
    for num in naomi:
        if ken[index] > num:
            index += 1
            counter += 1
    return num_of_blocks - counter

def war(case, num_of_blocks, naomi, ken):
    deceitful_win = deceitful(num_of_blocks, naomi, ken)
    normal_win = normal(num_of_blocks, naomi, ken)

    print_result(case, deceitful_win, normal_win)

def print_result(case, deceitful_win, normal_win):
    out_file.write("Case #" + str(case) + ": " + str(deceitful_win) + " " + str(normal_win) + '\n')

with open(file_name) as f:
    case_num = int(f.readline())
    for i in range(1, case_num + 1):
        num_of_blocks = int(f.readline())
        naomi = sorted(map(float, f.readline().strip().split(' ')), reverse=True)
        ken = sorted(map(float, f.readline().strip().split(' ')), reverse=True)
        war(i, num_of_blocks, naomi, ken)