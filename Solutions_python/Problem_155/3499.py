#!/usr/bin/evn python


def solve(cipher):
    input = cipher.split()
    
    number = 0
    needed = 0
    level = int(input[0])
    traversing_level =0

    really_needed = 0

    for j in input[1]:
        if j is not "0":
           if traversing_level > number:
               really_needed = (really_needed + traversing_level - number)
               number = number + really_needed
        number = number + int(j)
        traversing_level += 1
    return really_needed

    
if __name__ == "__main__":
    testcases = input()
    for caseNr in xrange(1, testcases+1):
        cipher = raw_input()
        print("Case #%i: %s" %(caseNr, solve(cipher)))

    
