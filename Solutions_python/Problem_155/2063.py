#!/usr/bin/env python
# -*- coding: utf-8 -*-

def solve(cipher):
	cipher = cipher.strip()
	number_of_level = int(cipher.split(" ")[0])
	number_of_people = cipher.split(" ")[1]
	sum_of_people = 0
	result = 0
	for i in xrange(number_of_level+1):
		diff = i - sum_of_people
		if 0 < diff:
			result += diff
			sum_of_people += diff

		cur_lvl_pep = int(number_of_people[i])
		sum_of_people += cur_lvl_pep
	return result
		

if __name__ == "__main__":
    testcases = input()
     
    for caseNr in xrange(1, testcases+1):
        cipher = raw_input()
        print("Case #%i: %s" % (caseNr, solve(cipher)))