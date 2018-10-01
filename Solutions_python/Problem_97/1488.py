'''
Created on Apr 14, 2012

@author: jon
'''

class GoogleFileReader(object):
    '''
    classdocs
    '''

    def __init__(self, filename):
        '''
        Constructor
        '''
        self.f = open(filename, 'r')
        self.n = int(self.f.next())
        
    def __iter__(self):
        return self
    def next(self):
        return self.f.next()