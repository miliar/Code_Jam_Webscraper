#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      poorb
#
# Created:     08/04/2017
# Copyright:   (c) poorb 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import sys
def resolve(text):
    arr = [int(ch) for ch in text]
    istydy = True
    lenarr = len(arr)
    while istydy:
        istydy = False
        if len(arr) == 1:
            break
        for i in range(lenarr-1 ):
            if arr[i] > arr[i+1]:
                arr[i] -= 1
                istydy = True
                for j in range(i+1, lenarr):
                    arr[j] = 9
    m = 1
    value = 0
    for idx in range(lenarr-1, -1, -1):
        value += arr[idx] * m
        m*=10
    return value


def read(r):
    n=int(r().strip() )
    answers =[ resolve( r().strip()) for i in range(n) ]

    return answers
def test(s):
    print("{0} => {1}",s, resolve(s) )
def test1():
    test("132")
def test2():
    test("1000")
def test3():
    test("7")
def test4():
    test("111111111111111110")
def test5():
    test("987654321987654321")
def main():
    if True:
        with open("B-large.in","r") as infile:
            answers = read(infile.readline)
        with open("TidyNumbers_out.txt","w") as outfile:
            for idx, answer in enumerate(answers):
                outfile.write("Case #{0}: {1}\n".format(idx+1, answer))
    else:
        test1()
        test2()
        test3()
        test4()
        test5()
if __name__ == '__main__':
    main()
