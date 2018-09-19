'''
Created on Apr 14, 2012

@author: jon
'''
import numpy as np
from FileReader import GoogleFileReader

class Googlers(object):
    def __init__(self, total_scores, num_surprising):
        self.ts = np.array(total_scores)
        self.ns = num_surprising
    
    def max_best_score(self, p):
        non_surprising_score = 3 * p - 2
        if p > 1:
            surprising_score = 3 * p - 4
        else:
            surprising_score = non_surprising_score
        num_non_surprising = (self.ts >= non_surprising_score).sum()
        num_pos_surprising = (self.ts >= surprising_score).sum() - num_non_surprising
        max_surprising = max(min(num_pos_surprising, self.ns), 0)
        return num_non_surprising + max_surprising

if __name__=="__main__":
    import sys; sys.argv=['','B-large.in','B-large.out']
    out = open(sys.argv[2],'w')
    fn = sys.argv[1]
    fr = GoogleFileReader(fn)
    for i, case in enumerate(fr):
        nums = np.array(case.split(),dtype=np.int32)
        g = Googlers(nums[3:], nums[1])
        n = g.max_best_score(nums[2])
        output = "Case #{}: {}".format(i+1, n)
        print output
        out.write(output + '\n')
        