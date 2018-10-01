'''
Created on Apr 13, 2012

@author: karnr
'''

def any_true(l):
    return reduce(lambda a, b: a or b, l)

def check_e_win(l, e):
    return any_true([e * 4 == r.replace('T', e) for r in l])

def get_all_combinations(l):
    comb = list(l)
    comb.extend([l[0][i] + l[1][i] + l[2][i] + l[3][i] for i in range(4)]) 
    comb.extend([l[0][0] + l[1][1] + l[2][2] + l[3][3], l[0][3] + l[1][2] + l[2][1] + l[3][0]])
    return comb
 
def _execute_test(test_input):
    comb = get_all_combinations(test_input)
    print comb
    for e in ('X', 'O'):
        if check_e_win(comb, e):
            return e + " won"
    
    if any_true([r.find('.') >= 0 for r in test_input]):
        return "Game has not completed"

    return "Draw"

def _parse_input(input_file):
    fh = open(input_file)
    num_of_tests = int(fh.readline().strip())
    count = 1
    test_data = dict()
    lines = fh.readlines()
    while (count <= num_of_tests):
        start_idx = 5 * (count - 1)
        end_idx = start_idx + 4
        test_data[count] = [l.strip() for l in lines[start_idx: end_idx]]
        count += 1
        
    fh.close()
    
    return test_data

def main():
    test_data_set = _parse_input("test_input")
    num_of_tests = len(test_data_set.keys())
    
    output = open("test_output", "w")
    for test_id in xrange(1, num_of_tests + 1):
        test_data = test_data_set[test_id]
        test_result = _execute_test(test_data)
        output.write("Case #%s: %s\n" % (test_id, test_result))
        
    output.close()
    
if __name__ == '__main__':
    main()