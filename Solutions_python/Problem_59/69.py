'''
Created on May 22, 2010

@author: AliJ
'''

def parse_num():
    return map(int, raw_input().split())

numCases = int(raw_input())

def process_case():
    (N,M) = parse_num()
    
    current = {}
    
    for i in range(N):
        path = raw_input().lstrip('/').split('/')
        if path[0] not in current:
            current[path[0]] ={}
        
        prevLevel = current[path[0]]
        
        for j in range(1, len(path)):
            if path[j] not in prevLevel:
                prevLevel[path[j]] = {}
            
            prevLevel = prevLevel[path[j]]
            
    count = 0
    for i in range(M):
        path = raw_input().lstrip('/').split('/')
        if path[0] not in current:
            count +=1
            current[path[0]] ={}
        
        prevLevel = current[path[0]]
        
        for j in range(1, len(path)):
            if path[j] not in prevLevel:
                count +=1
                prevLevel[path[j]] = {}
            
            prevLevel = prevLevel[path[j]]
        
    return count
        

for i in range(numCases):
            
    print "Case #"+str(i+1)+":", (process_case())