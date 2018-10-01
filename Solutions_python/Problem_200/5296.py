#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  8 13:11:12 2017

@author: Jiayi Chen
"""
def tidy(N):
    N = int(N)
    tidy = check_tidy(abs(N))
    #print("tidy is",tidy)
    while not tidy:
        N = N - 1
        tidy = check_tidy(N)
    return N

def check_tidy(N):
    try:
        #print(N)
        string = str(N)
        length = len(str(N))
        if abs(N)<10:
            return True
        elif int(string[length-1]) >= int(string[length-2]):
            #print(int(string[length-1]), ">", int(string[length-2]))
            #print(int(string[:length-1]))
            #print(check_tidy(int(string[:length-1])))
            return(check_tidy(int(string[:length-1])))
        else:
            #print(int(string[length-1]), "<", int(string[length-2]))
            #print("not tidy")
            return False
    except TypeError:
        return "string in input"

if __name__ == '__main__':
    f = open("B-small-attempt0.in")
    num = int(f.readline())
    cnt = 1
    N = int(f.readline())
    while cnt <= num:
        print("Case #{}:".format(cnt), tidy(N))
        N = f.readline()
        cnt += 1
    f.close()
