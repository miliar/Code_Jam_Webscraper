'''
Created on 8 avr. 2017

@author: franc
'''

class PancakePile():
    '''
    classdocs
    '''
    pile = []
    panSize = 0
    flipCount = 0


    def __init__(self, panSize):
        '''
        Constructor
        '''
        self.panSize = panSize
        self.pile = []
        self.flipCount = 0
        
    def addPancake (self, pancake):
        self.pile.append(pancake)
    
    def flipFrom(self, index):
        print ("flip " + str(index))
        if(len(self.pile) - index >= self.panSize): 
            for x in range(index, index + self.panSize):
                print(str(x) + " "+ str(self.pile[x].smilling) + "")
                self.pile[x].flip()
            return True
        else:
            return False
    def firstBlankSide(self):
        for x in range(len(self.pile)):
            if not self.pile[x].smilling:
                return x
    
        
    def allUp(self, begin = 0, end =0):
        if(begin == end):
            for panck in self.pile :
                if not panck.smilling:
                    return False
        else:
            if(end < len(self.pile)) :
                for x in range(begin, end):
                    if not self.pile[x].smilling:
                        return False
            else :
                print ("end index  greater than pile size")
                return False
        return True
    
    def allDown(self, begin = 0, end =0):
        if(begin == end):
            for panck in self.pile :
                if panck.smilling:
                    return False
        else:
            if(end < len(self.pile)) :
                for x in range(begin, end):
                    if self.pile[x].smilling:
                        return False
            else :
                print ("end index  greater than pile size")
                return False
        return True
    
    def countSmilling(self):
        count = 0
        for panck in self.pile:
            if (panck.smilling):
                count = count +1
        return count;
    
    def reducePile(self):
        #print ("before " + str(len(self.pile)) + " index " + str(self.firstBlankSide()))
        beginIndex = self.firstBlankSide()
        self.pile =  self.pile[beginIndex:]
        #print ("after " + str(len(self.pile)))
       
    def isPossible(self):
        if not self.allUp():
            if self.panSize > len(self.pile) :
                return False
            if len(self.pile) < 2*self.panSize-1:
                begin = len(self.pile) - self.panSize
                end   = self.panSize - 1
                return (self.allUp(begin, end) or self.allDown(begin, end))
            else :
                return True
        else : 
            return True
        
    
    
    def printPile(self):
        out=""
        for x in self.pile:
            if x.smilling:
                out+="1"
            else :
                out+= "0"
        print (out)
    def solve(self):
        count = 0
        alldown = False
        while(not (self.allUp() or not self.isPossible())):
            self.flipFrom(self.firstBlankSide())
            count += 1
            self.reducePile()
            self.printPile()
            #if alldown:
            #    quit()
            #alldown = self.allDown()
            
        if(not self.isPossible()):
            print("IMPOSSIBLE")
            return "IMPOSSIBLE"
        else:
            return count
