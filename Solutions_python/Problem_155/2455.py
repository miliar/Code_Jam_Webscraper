__author__ = 'Vishal Gupta'

def audience(max_shy, a_shy):
    if (a_shy) == "":
        return 0
    zeroes = []
    audience_count = 0
    outside_count = 0
    for idx in xrange(int(max_shy) + 1):
        dummy_loop = int(a_shy[idx])
        if (dummy_loop == 0):
            zeroes.append([idx, dummy_loop])
        elif (idx <= audience_count):
            audience_count += dummy_loop
        else:
            zeroes[0][1] += idx - audience_count
            outside_count += idx - audience_count
            audience_count += idx - audience_count
            audience_count += dummy_loop
    return outside_count

if __name__ == "__main__":
    inputfile = open("C:/Users/Admin/Desktop/A-large.in","r")
    outputfile = open("C:/Users/Admin/Desktop/output_A_large.txt", "w+")
    testcases = int(inputfile.readline())
    for dummy_testcases in xrange(1, testcases + 1):
        in_str = inputfile.readline()
        case = in_str.split()
        final_count = audience(case[0], case[1])
        out_str = "Case #{}: {}\n".format(dummy_testcases, final_count)
        outputfile.write(out_str)
    inputfile.close()
    outputfile.close()