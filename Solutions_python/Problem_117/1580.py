# Lawnmower

import sys

def get_sorted_v_h_lines(lines, num_row, num_col):
    vlines = []
    hlines = []    
    i = 0
    j = 0
    hlines_done = False

    while j < num_col:
        i = 0
        my = []
        while i < num_row:
            if hlines_done == False:
                hlines.append(list(lines[i]))
                hlines[-1].sort()
            my.extend(lines[i][j])
            i += 1
        vlines.append(my)
        vlines[-1].sort()
        j += 1
        hlines_done = True
    
    return hlines, vlines
    

def get_match_result(lines, n, m):
    i = 0
    j = 0
    
    s_hlines, s_vlines = get_sorted_v_h_lines(lines, n, m)

    # print lines
    # print "\n"
    # print s_hlines
    # print "\n"
    # print s_vlines
    # print "\n"


    while i < n:
        j = 0
        while j < m:
            if (s_hlines[i][-1] > lines[i][j]):
                if (s_vlines[j][-1] > lines[i][j]):
                    return "NO"
            j += 1
        i += 1
    return "YES"

def compute_results(inbuff, outfd):
    in_cases = int(inbuff[0])
    inbuff = inbuff[1:]
    j = 0
    output = ""
#    in_cases = 1

    for i in range(0, in_cases):
        lines = []
        size = inbuff[j]
        j += 1
        n, m = size.strip().split()
        n = int(n)
        m = int(m)

        p = 0
        while p < n:
            lines.append(inbuff[j].strip().split(' '))
            j += 1
            p += 1
        result = get_match_result(lines, n, m)
        obuffer = "Case #%d: %s\n" %(i+1, result)
        output += obuffer

    outfd.write(output)

if __name__ == "__main__":
    input = sys.argv[1]
    
    infd = open(input, "r")
    inbuff = infd.readlines()
    
    infd.close()

    outfd = open("output.txt", "w+")
    
    compute_results(inbuff, outfd)
    outfd.close()
    
