import os
import math


def is_palindrome(num):
    x = str(num)
    x_letters = [c for c in x]
    res = (x_letters == x_letters[::-1])
    return res

def main():
    f = open("C-small-attempt4.in","r")
    doc = f.read().split('\n')   
    num_test_cases = int(doc[0])
    numa = []
    numb = []
    for i in range(0, num_test_cases):
        numbers = doc[i+1].split(" ")
        numa.append(int(numbers[0]))
        numb.append(int(numbers[1]))
        
    for i in range(0, num_test_cases):
        #Get the base minimum square number
        output = 0
        min_sq_num     =   math.sqrt(numa[i])
        max_sq_num     =   math.sqrt(numb[i])

        int_min_sq_num =   int(min_sq_num)
        int_max_sq_num =   int(max_sq_num)      
        
        if (int_min_sq_num == int_max_sq_num):
            if is_palindrome(int_min_sq_num) is True:
                if is_palindrome(int_min_sq_num*int_min_sq_num) is True:
                    output = output +1
            print "Case #"+str(i+1)+": "+str(output)
            continue
            


        if ((min_sq_num-int(min_sq_num)) == 0):
            if is_palindrome(int_min_sq_num) is True:
                if is_palindrome(int_min_sq_num*int_min_sq_num) is True:
                    output = output +1
                    
            min_to_start = int_min_sq_num+1
        else:
            min_to_start    =  int_min_sq_num + 1
            
        

        if ((max_sq_num-int(max_sq_num)) == 0):
            if is_palindrome(int_max_sq_num) is True:
                if is_palindrome(int_max_sq_num*int_max_sq_num) is True:
                    output = output +1
        else:
            int_max_sq_num = int_max_sq_num+1 
        

        for each_num in range(min_to_start, int_max_sq_num):
            square  = each_num*each_num
            if square in range(numa[i],numb[i]+1):
                if is_palindrome(each_num) is True:
                    if is_palindrome(each_num*each_num) is True:
                        output = output +1
                        #print each_num
                    
        print "Case #"+str(i+1)+": "+str(output)        
        
            

if __name__ == "__main__":
    main()
