#!/usr/bin/env python3
dictionary = { 'a':'y' , 'b':'h', 'c':'e', 'd':'s', 'e':'o', 'f':'c', \
               'g':'v', 'h':'x' ,'i':'d', 'j':'u', 'k':'i', 'l':'g', ' ':' ', \
               'm':'l', 'n':'b', 'o':'k', 'p':'r', 'q':'z', 'r':'t', \
               's':'n', 't':'w', 'u':'j', 'v':'p', 'w':'f', 'x':'m', 'y':'a', 'z':'q' } 


def solve(I):
    result = ""
    for x in I:
        y = dictionary[x]
        result = result + y
    return result


if __name__ == "__main__":
    T = int(input());
    for c in range(T):
        I = input().strip()
        R = solve(I)
        print("Case #{}: {}".format(c+1,R))
