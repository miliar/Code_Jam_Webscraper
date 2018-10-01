'''
Created on Sep 26, 2009

@author: AliJ
'''

def parse_num():
    return map(int, raw_input().split())

def swap(M, i, j):
    temp = M[i]
    M[i]= M[j]
    M[j] =temp
    
def NoOnes(M, row, k):
    for i in range(k+1, len(M)):

        if M[row][i] == "1":
            return False
        
    return True 
         
def findGood(M, row):
    for i in range(row, len(M)):
        if NoOnes(M, i, row):

            return i
    
    return -1

def moveToRow(M, dest, source):
    for i in range(source, dest, -1):
        swap(M, i, i-1) 
        
      

def process_case():
    N = int(raw_input())
    M=[]
    for i in range(N):
        nextRow = raw_input().strip()
        M.append(nextRow)
        

        
    numSwaps = 0
    for i in range(N):
        if not NoOnes(M, i, i):
            source= findGood(M, i)
            moveToRow(M, i, source)
            numSwaps += (source - i)
            
    return numSwaps
        
    
        
    

numCases = int(raw_input())

for i in range(numCases):
            
    print "Case #"+str(i+1)+":", (process_case())