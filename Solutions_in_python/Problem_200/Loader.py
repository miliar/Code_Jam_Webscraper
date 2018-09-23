'''
Created on 8 avr. 2017

@author: franc
'''

class Loader():
    '''
    classdocs
    '''
    
    filename = ""
    file = None


    def __init__(self, filename):
        '''
        Constructor
        '''
        self.filename = filename
        self.file = open(filename, 'r' )
        
    def returnDataArray(self):
        first = True
        index = 0;
        output = {}
        for line in self.file:
            print(line)
            if first:
                output["NB"] = str(line.replace("\n",""))
                first = False
            else:
                output["Case #" + str(index) + ": "]  = line.replace("\n","").split(" ")
            index = index+1
                
        return output