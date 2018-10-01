import sys
from itertools import combinations


def parse(file_name):
    in_data = open(file_name).readlines()
    fixed_data = [line.strip() for line in in_data]
    return fixed_data[1:]

def group_data(data):
    tests = []
    while len(data) > 0:
        data.pop(0)
        stack = data.pop(0).split()
        stack = [int(value) for value in stack]
        tests.append(stack)
    return tests

def add(candy1, candy2):
    bin_candy1 = bin(candy1)[2:]
    bin_candy2 = bin(candy2)[2:]
    #print bin_candy1, bin_candy2
    bin_candy1=bin_candy1[::-1]
    bin_candy2=bin_candy2[::-1]
    if len(bin_candy2) > len(bin_candy1):
        bin_candy1, bin_candy2 = bin_candy2, bin_candy1
    result = ""
    
    for index in range(len(bin_candy1)):
        if index < len(bin_candy2):
            if bin_candy1[index] == bin_candy2[index]:
		result = "0" + result
            else:
                result = "1" + result
        else:
            result = bin_candy1[index] + result
    #print "0b" + result
    return int("0b" + result,2)

def sean_value(pile):
    sum_of_candy = 0
    for candy in pile:
        sum_of_candy = add(sum_of_candy, candy)
    return sum_of_candy


data = parse(sys.argv[1])
tests = group_data(data)
case = 0
for test in tests:
    case = case + 1
    bag = test
    max_value = 0
    for size in range(1, len(bag)):
        for combination in combinations(bag, size):
            pile_2 = []
            pile_2.extend(bag)
            #print combination
            #print pile_2
            for candy in combination:
                pile_2.remove(candy)
            #print pile_2
            if sean_value(combination) == sean_value(pile_2):
                #print combination, sean_value(combination), " == ", pile_2, sean_value(pile_2)
                max_value = max(max_value, max(sum(combination), sum(pile_2)))
    if max_value == 0:
        print "Case #" +  str(case) +": NO"
    else:
        print "Case #" +  str(case) +": " + str(max_value)
