'''
Created on Apr 12, 2014

@author: Ardi
'''

class MagicTricksSolver(object):
    '''
    classdocs
    '''
    
    def __init__(self, choice1, cards1, choice2, cards2):
        '''
        Constructor
        '''
        self._choice1 = choice1
        self._cards1 = cards1
        self._choice2 = choice2
        self._cards2 = cards2
        
    def _getSetFromChoice(self, choice, cards):
        cardSet = set(cards[choice-1])
        #print(cardSet)
        return cardSet
        
    def solve(self):
        set1 = self._getSetFromChoice(self._choice1, self._cards1)
        set2 = self._getSetFromChoice(self._choice2, self._cards2)
        guessSet = set1 & set2
        #print(guessSet)
        guessSetSize = len(guessSet)
        if guessSetSize == 1:
            ret = guessSet.pop()
            return str(ret)
        elif guessSetSize > 1:
            return 'Bad magician!'
        elif guessSetSize == 0:
            return 'Volunteer cheated!'
            