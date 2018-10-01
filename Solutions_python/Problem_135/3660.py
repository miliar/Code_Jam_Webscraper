#!/usr/bin/env python
# encoding: utf-8

__author__ = 'nikola'

def solve(data):
    g1=int(data[0])
    c1=[[int(i) for i in x.split()] for x in data[1:5]]
    g2=int(data[5])
    c2=[[int(i) for i in x.split()] for x in data[6:]]

    intersection=list(set(c1[g1-1]).intersection(c2[g2-1]))

    if len(intersection)==0:
        return "Volunteer cheated!"
    elif len(intersection)==1:
        return intersection[0]
    else:
        return "Bad magician!"


def main():
    with open("input.txt",'r') as in_file, open('output.txt','w') as out_file:
        case_count=int(in_file.readline())
        cases=in_file.read().splitlines()
        for i in xrange(case_count):
            index=i*10
            result=solve(cases[index:index+10])
            out_file.write("Case #{}: {}\n".format(i+1, result))

    pass

if __name__ == "__main__":
    main()