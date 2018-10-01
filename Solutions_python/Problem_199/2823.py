'''
Created on April 12, 2014

@author: Lior
'''


def solve(k, pancakes):
    s = len(pancakes)
    pancakes = list(pancakes)
    result = 0
    for i in range(s - k + 1):
        if pancakes[i] == "+":
            continue
        result += 1
        for j in range(k):
            if pancakes[i+j] == "+":
                pancakes[i+j] = "-"
            else:
                pancakes[i+j] = "+"

    if pancakes == ["+"]*s:
        return str(result)
    else:
        return "IMPOSSIBLE"





def process_files(in_file, out_file):
    num_of_test_cases = int(in_file.next().strip())
    #for test_number in xrange(num_of_test_cases):
    #    line = in_file.next()
    #    result = solve(N)
    #    out_file.write('Case #%d: %s\n' % (test_number+1, result))
    i = 0
    for line in in_file:
        i += 1
        pancakes, k = line.split(" ")
        k = int(k)
        result = solve(k, pancakes)
        out_file.write("Case #" + str(i) + ": " + result + "\n")







if __name__ == '__main__':
    import sys, os
    in_file = sys.argv[1]
    out_file = in_file.replace('.in', '.out')
    with open(in_file, 'rb') as in_file:
        with open(out_file, 'wb') as out_file:
            process_files(in_file, out_file)
