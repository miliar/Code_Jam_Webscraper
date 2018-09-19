'''
Created on Sep 3, 2009

@author: Aaron
'''

class Word:
    '''
    Word Class
    '''


    def __init__(self, num_chars, chars):
        '''
        Constructor
        '''
        self._num_chars = num_chars
        self._chars = chars.strip()
        
    def match_pattern(self, pattern):
        for _index in range(len(self._chars)):
            if (self._chars[_index] not in pattern.get_token(_index).get_chars()):
                return False
        return True
    