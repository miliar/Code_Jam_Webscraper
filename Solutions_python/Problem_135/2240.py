#!python
#-*- encoding:utf-8 -*-
import sys

def solve(first_row, first_list, second_row, second_list):
    f = first_list[first_row]
    s = second_list[second_row]
    matched = [y for y in f for x in s if x == y]
    if len(matched) is 0:
        return "Volunteer cheated!"
    elif len(matched) is 1:
        return str(matched[0])
    else:
        return "Bad magician!"
    pass

if __name__ == "__main__":
    cases = int(raw_input())
    for i in range(cases):
        first_row = int(raw_input()) - 1
        first_list = [map(int, raw_input().split()) for j in range(4)]
        second_row = int(raw_input()) - 1
        second_list = [map(int, raw_input().split()) for j in range(4)]
        result = solve(first_row, first_list, second_row, second_list)
        print "Case #{0}: {1}".format(i+1, result)
