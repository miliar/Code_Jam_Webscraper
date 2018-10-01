import sys

def read_test_cases(input_file_name):
    test_cases = []

    f = open(input_file_name)

    T = int(f.readline())

    for i in xrange(T):
        raw_test_case = f.readline()[:-1]
        splitted = raw_test_case.split(" ")

        C = int(splitted[0])

        combined = []
        for j in xrange(C):
            combined.append(list(splitted[1 + j]))

        D = int(splitted[C + 1])

        opposed = []
        for j in xrange(D):
            opposed.append(list(splitted[C + 2 + j]))

        base_element_list = list(splitted[-1])

        test_case = {}
        test_case['combined'] = combined
        test_case['opposed'] = opposed
        test_case['base_element_list'] = base_element_list

        test_cases.append(test_case)
    
    f.close()

    return test_cases

def write_results(output_file_name, results):
    f = open(output_file_name, 'wt')

    for i, result in enumerate(results):
        result_str = str(result).replace("'", "")
        f.write("Case #%d: %s\n" % (i + 1, result_str))

    f.close()

def get_element_list(test_case):
    combined = test_case['combined']
    opposed = test_case['opposed']
    base_element_list = test_case['base_element_list']

    element_list = []

    for el in base_element_list:
        is_combined = False
        is_opposed = False

        # combine
        if len(element_list) > 0:
            last_el = element_list[-1]
            for c in combined:
                if (c[0] == el and c[1] == last_el) or (c[0] == last_el and c[1] == el):
                    element_list[-1] = c[2]
                    is_combined = True
                    break

        if is_combined:
            continue
        # opposed
        opposed_elements = []
        for op in opposed:
            if op[0] == el:
                opposed_elements.append(op[1])
            elif op[1] == el:
                opposed_elements.append(op[0])

        for op in opposed_elements:
            if op in element_list:
                element_list = []
                is_opposed = True
                break
        if is_opposed:
            continue

        element_list.append(el)

    return element_list

def main():
    assert len(sys.argv) == 3

    input_file_name = sys.argv[1]
    output_file_name = sys.argv[2]

    test_cases = read_test_cases(input_file_name)

    results = []

    for test_case in test_cases:
        element_list = get_element_list(test_case)
        results.append(element_list)

    write_results(output_file_name, results)
        

if __name__ == "__main__":
    main()
