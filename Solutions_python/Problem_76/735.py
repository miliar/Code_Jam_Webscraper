#!/usr/bin/env python

from __future__ import print_function
import sys

import itertools


def xor_list(list):
    final_xor = list[0]
    for value in list[1:]:
        final_xor = final_xor ^ value
    return final_xor

def find_biggest_pile(list):
    greatest_sum = -1

    equal_pile = len(list)/2+1
    for i in xrange(1,equal_pile):
        # print("pile1 size:", i)
        possible_pile1 = itertools.combinations(list, i)
        for pile1 in possible_pile1:
            pile2 = []
            for value in list:
                pile2.append(value)
            for value in pile1:
                # print(value)
                pile2.remove(value)

            # print("Pile 1:", pile1)
            # print("Pile 2:", pile2)

            pile1_sum = sum(pile1)
            pile2_sum = sum(pile2)
            pile1_xor = xor_list(pile1)
            pile2_xor = xor_list(pile2)

            if(pile1_xor == pile2_xor):
                if(pile1_sum > greatest_sum):
                    greatest_sum = pile1_sum
                if(pile2_sum > greatest_sum):
                    greatest_sum = pile2_sum

    if(greatest_sum == -1):
        return "NO"
    else:
        return str(greatest_sum)

def main(*args):
    if(len(args) < 2):
        print("Usage: %s <input file>" % args[0])

    filename = args[1]
    input_file = open(filename, "rb")
    output_file = open(filename+".out", "wb")

    try:
        input = input_file.readline().strip()
    except:
        print("Premature end of input")

    T = int(input)
    for i in range(T):
        try:
            input = input_file.readline().strip()
            N = int(input)
            inputs = input_file.readline().split()
        except:
            print("Premature end of input")

        values = []
        for value in inputs:
            values.append(int(value))
        # print(values)
        output = find_biggest_pile(values)
        print("Case #%d: %s" % (i+1, output),file=output_file)

    input_file.close()
    output_file.close()


if(__name__ == "__main__"):
    sys.exit(main(*sys.argv))
