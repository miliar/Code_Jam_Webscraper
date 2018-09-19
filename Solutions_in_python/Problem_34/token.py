'''
Created on Sep 3, 2009

@author: Aaron
'''

class Token:
    '''
    Token Class
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self._dynamic = False
        self._chars = ''
        
    def set_dynamic(self):
        self._dynamic = True
        
    def is_dynamic(self):
        return self._dynamic
        
    def get_chars(self):
        return self._chars
        
    def add_char(self, char):
        self._chars = self._chars + char
    