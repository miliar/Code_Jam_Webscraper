#! /usr/bin/env python

def print_result(array):
    return str(array).replace('\'', '')

if __name__== "__main__":
    testcases = int(input())
    for t in range(testcases):
        combine = {}
        opposed = {}
        elem_list = []
        
        line = raw_input()
        line = line.split()
        
        c = int(line[0])
        line = line[1:]
        for i in range(c):
            elem = line[i]
            combine[elem[0]] = { elem[1]: elem[2] }
            combine[elem[1]] = { elem[0]: elem[2] }
        
        d = int(line[c])
        line = line[c+1:]
        for i in range(d):
            elem = line[i]
            opposed[elem[0]] = elem[1]
            opposed[elem[1]] = elem[0]
        
        word = line[len(line)-1]
        elem_list.append(word[0])
        for char in word[1:]:
            if not elem_list:
                elem_list.append(char)
                continue
            last_elem = elem_list[len(elem_list)-1]
            if char in combine:
                if last_elem in combine[char]:
                    elem_list.pop()
                    elem_list.append(combine[char][last_elem])
                    continue
            if char in opposed:
                if opposed[char] in elem_list:
                    elem_list = []
                    continue
            elem_list.append(char)
        print "Case #%d: %s" % (t+1, print_result(elem_list))

