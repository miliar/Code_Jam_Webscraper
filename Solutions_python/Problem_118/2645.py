import math

def isPalindrome(num):
# gets a number and checks if its Palindrome 
     x = num;
     y = 0;
     while (num > 0):
          dig = num % 10;
          y = y * 10 + dig;
          num = num / 10;
     if x==y:
        return True

def isSquare(num):
# gets a number and checks if its square  
     x = math.sqrt(num)
     if ((x * 10) % 10) == 0.0:
        return True

def countFairAndSquare(a, b):
    
    count = 0
    for i in range(a, b + 1):
       if (isPalindrome(i) and isSquare(i)):   
           if (isPalindrome(int(math.sqrt(i)))):
               count += 1
    return count

with open("C-small-attempt0.in") as f:
    data = f.readlines()
    cases = int(data[0])

for i in range(cases):
    #program starts here
    a = int(data[1:][i].split(" ")[0])
    b = int(data[1:][i].split(" ")[1])
    
    print "Case #%s: %s" % ((i + 1), countFairAndSquare(a, b))
    
        
    
   