import re

testcases = int(input())

def check_consonants(name, n):
    consonants = 0
    const = "[bcdfghjklmnpqrstvwxyz]"
    const = [const for i in range(n)]
    const = ''.join(const)
    
    reg = r"("+const+")+"
    if(re.search(reg, name)):
        return True
        
    else:
        return False
        
for case in range(1, testcases+1):
    name = input().split()
    n = int(name[1])
    name = name[0]
    val = 0
    for start in range(len(name)):
        for end in range(start, len(name)):
            if(check_consonants(name[start:end+1], n)):
                val += 1
                
    print("Case #"+str(case)+": "+str(val))