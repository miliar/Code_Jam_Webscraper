'''
Created on 11.04.2015

@author: uscheller
'''
import sys


def solve(s_max, shyness_list):
    additional_people = 0
    currently_standing = 0
    last_standing = 0
    audience = sum(shyness_list)
    
    while currently_standing < audience:
        for i in range(min(currently_standing + additional_people + 1, s_max + 1)):
            if shyness_list[i] > 0:
                currently_standing += shyness_list[i]
                shyness_list[i] = 0
        if currently_standing == last_standing:
            additional_people += 1
        last_standing = currently_standing
    return additional_people
        

def go_through(data):
    data = data[1:]
    s = ""
    for case, line in enumerate(data):
        s_max, shyness_list = line.split()
        shyness_list = [int(x) for x in shyness_list]
        s += "Case #%d: %d\n" % (case + 1, solve(int(s_max), shyness_list))
    return s[:-1] # remove newline

if __name__ == '__main__':
    print go_through(open(sys.argv[1]).readlines())