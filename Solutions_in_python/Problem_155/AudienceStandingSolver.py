'''
Created on 24 Mar 2015

@author: dev
'''

class AudienceStandingSolver:
    
    

    
    def solve(self, S):
        Sint = [int(s) for s in S]
        result = self.algorithm(Sint)
        return str(result)

    
    def algorithm(self, Sint):
        added = 0
        standing = 0 
        for i in range(len(Sint)):
            addedTemp = 0
            if standing < i and Sint[i] != 0:
                addedTemp = (i - standing)
                added = added + addedTemp  
            standing = standing + Sint[i] + addedTemp
        return added 

'''    
4
4 11111
1 09
5 110011
0 1
'''