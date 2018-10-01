from math import sqrt, ceil

cases = int(raw_input())
case = 1

def nextPalindrome(n):
    
    n = str(n)
    l = 0
    u = len(n) - 1
    
    while l < u:
        a, b = int(n[l]), int(n[u])
        if a > b:
            n = n[:l] + str(a) + n[l + 1:u] + str(a) + n[u + 1:]
        elif b > a:
            n = n[:l] + str(a + 1) + n[l + 1:u] + str(a + 1) + n[u + 1:]
        
        l += 1
        u -= 1
    
    return n

def getPalindromes(slower, supper):
    current = nextPalindrome(slower)
    length = len(current)
    palindromes = []
    done = False
    
    if length % 2 == 0:
            checkup = length / 2
            checkdown = checkup - 1
    else:
        checkup = length / 2
        checkdown = checkup
    
    while True:
        nocheck = False
        if int(current) > supper:
            break
        else:
            palindromes.append(int(current))
        
        while current[checkup] == "9":
            
            if checkdown == 0:
                current = str(10 ** (checkup + 1) + 1)
                length += 1
                if length % 2 == 0:
                        checkup = length / 2
                        checkdown = checkup - 1
                else:
                    checkup = length / 2
                    checkdown = checkup
                nocheck = True
            else:
                if checkdown == checkup:
                    current = current[:checkdown] + "0" + current[checkup + 1:]
                else:
                    current = current[:checkdown] + "0" + current[checkdown + 1:checkup] + "0" + current[checkup + 1:]
                checkup += 1
                checkdown -= 1
                
        if not nocheck:
            num = int(current[checkup]) + 1
            if checkdown == checkup:
                current = current[:checkdown] + str(num) + current[checkup + 1:]
            else:
                current = current[:checkdown] + str(num) + current[checkdown + 1:checkup] + str(num) + current[checkup + 1:]
                
    return palindromes
    
def isPalindrome(n):
    
    n = str(n)
    l = 0
    u = len(n) - 1
    
    while l < u:
        if n[l] != n[u]:
            return False
        
        l += 1
        u -= 1
    
    return True
    
while case <= cases:
    lower, upper = [int(i) for i in raw_input().split()]
    
    slower = int(ceil(sqrt(lower)))
    supper = int(sqrt(upper))
    
    palindromes = getPalindromes(slower, supper)
    
    count = 0
    for palindrome in palindromes:
        if isPalindrome(palindrome ** 2):
            count += 1
            
    print "Case #" + str(case) + ": " + str(count)
    case += 1
