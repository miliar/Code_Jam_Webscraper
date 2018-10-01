

import sys

class Staller():
    def __init__(self,stalls,shitters):
        self.stalls = stalls
        self.shitters = shitters
        self.count = 0
        self.answer = None
        self.numlist=[]
        #halving the problem
        '''
        while self.both_even():
            self.shitters /= 2
            self.stalls /= 2
        '''
        '''
        if self.shitters>(self.stalls+1)/2:
            self.answer=[0,0]
        '''
        self.numlist.append(self.stalls)
        self.prev_num_lst = []


    def both_even(self):
        return self.stalls % 2 == 0 and self.shitters % 2 == 0



    def transform(self):
        if self.count == self.shitters:
            self.answer = sorted(self.prev_num_lst,reverse=True)
            return
        else:
            self.count +=1
            self.numlist.sort()
            num=self.numlist.pop(-1)
            if num % 2 == 0:
                self.prev_num_lst = [num / 2 for i in range(2)]
                self.prev_num_lst[0] -= 1
                for i in self.prev_num_lst:
                    self.numlist.append(i)
            else:
                num -= 1
                self.prev_num_lst = [num / 2 for i in range(2)]
                for i in self.prev_num_lst:
                    self.numlist.append(i)
            self.transform()


def main():
    sys.setrecursionlimit(50000)
    n = int(raw_input())
    for case in range(1, n + 1):
        n,k = map(int,raw_input().split(" "))
        stallobj=Staller(n,k)
        if stallobj.answer is None: stallobj.transform()
        print "Case #{}: {} {}".format(case, stallobj.answer[0], stallobj.answer[1])

main()