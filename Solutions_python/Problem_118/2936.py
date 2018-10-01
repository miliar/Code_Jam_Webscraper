import os
import math

def is_palindrome(w):
    w = str(w)
    
    while w and w[0] == w[-1]:
        w = w[1:-1]
    return w == ""
    
     
    

in_file = open(os.path.join(os.path.expanduser("~"), "Downloads/C-small-attempt0.in"), "r")
out_file = open(os.path.join(os.path.expanduser("~"), "Downloads/c.data.out"), "w")

cases = int(in_file.readline())

for case in range(cases):
    start, end = map(int , in_file.readline().split())
    count = 0
    
    for  j in range(start, end+1):
        if is_palindrome(j):
            t = math.sqrt(j)
            print j, t.is_integer() , is_palindrome(int(t))
            if t.is_integer() and is_palindrome(int(t)):
                count += 1
    out_file.write("Case #%d: %s\n" %(case +1, count))
        