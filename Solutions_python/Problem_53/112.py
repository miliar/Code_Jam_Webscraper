'''
Created on May 8, 2010

@author: AliJ
'''

def parse_num():
    return map(int, raw_input().split())

numCases = int(raw_input())

def process_case():
    (N,K)=parse_num()
    if (K+1)%(2**N)==0:
        return "ON"
    else:
        return "OFF"

for i in range(numCases):
            
    print "Case #"+str(i+1)+":", (process_case())
