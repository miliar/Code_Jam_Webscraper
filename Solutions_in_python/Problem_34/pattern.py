'''
Created on Sep 3, 2009

@author: Aaron
'''

from alien import token

class Pattern:
    '''
    Pattern Class
    '''


    def __init__(self, num_tokens, pattern):
        '''
        Constructor
        '''
        self._num_tokens = num_tokens
        self._pattern = pattern.strip()
        self._tokens = []
        
        _token = token.Token()
        for _index in range(len(self._pattern)):
            if (self._pattern[_index] == '('):
                _token.set_dynamic()
                continue
            if (self._pattern[_index] == ')'):
                self._tokens.append(_token)
                _token = token.Token()
                continue
            _token.add_char(self._pattern[_index])
            if (not _token.is_dynamic()):
                self._tokens.append(_token)
                _token = token.Token()
        
    def get_token(self, index):
        return self._tokens[index]
    