# XOR is key!!!

class Solution(object):
    
    # Please don't change these four constants.
    HAPPY = 0
    DOWN  = 1
    
    HAPPY_char = '+'
    DOWN_char  = '-'
    
    
    # O(N) time
    # - Let N == len(pancakes)
    # - Let K == flipper_length
    def min_flips(self, pancakes, flipper_length):
        
        # 2 <= flipper_length <= len(pancakes)
        
        # encode the pancakes and the flipper as binary numbers each
        bin = self.get_bin(pancakes) # O(N)
        flipper = self.get_flipper_bin(flipper_length) #O(K)
        
        num_flips_soFar = 0
        
        # O(N)
        while bin > 0:
            
            # work from the right to the left
            
            while LSB(bin) == self.HAPPY:
                bin >>= 1
            
            if bit_length(bin) < bit_length(flipper):
                return 'IMPOSSIBLE'
            
            # apply the flipper
            bin ^= flipper
            
            num_flips_soFar += 1
        
        # bin == 0
        
        return num_flips_soFar
    
    # Returns a number that has up to N == len(pancakes) bits (leading zeros are thrown out)
    # Good thing Python handles arbitrarily large integers seamlessly
    def get_bin(self, pancakes):
        """
        For pancakes ==  '+--+-',
          returns 13 == 0b01101
        """
        
        B = 2
        num = 0
        
        for char in pancakes:
            num *= B
            if char is self.DOWN_char:
                num += self.DOWN
        return num
    
    def get_flipper_bin(self, flipper_length):
        """
        Ror flipper_length == 3,
          returns 0b111
        
        For flipper_length == 8,
          returns 0xff == 0b11111111
        
        etc...
        """
        
        assert flipper_length > 0
        
        B = 2
        f = 0
        for i in range(flipper_length):
            f *= B
            f += 1
        return f


def LSB(bin):
    LSB_mask = 0b1 # least significant bit mask
    return bin & LSB_mask


def bit_length(num):
    return len( bin(num)[2:] ) # [2:] skips the '0b'
    
    # preferred not to use log2