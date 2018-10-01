#!/usr/bin/python

import math

class numbers:
    def __init__(self, from_val, to_val):
        self.from_val = from_val
        self.to_val = to_val
        self.val_range = to_val - from_val
        
        self.bits = 16
        self.numbers = [0 for row in range(int(math.ceil(1.0 * (self.val_range + 1) / self.bits)))]
        self.max_val = int(math.exp(self.bits * math.log(2)))

    def __contains__(self, value):
        if value < self.from_val or value > self.to_val:
            return False
        
        value -= self.from_val
        lineIx = value / self.bits
        mask = self.get_mask(value)

        if self.numbers[lineIx] & mask > 0:
            return True
        else:
            return False

    def get_mask(self, value):

        lineIx = value / self.bits
        bitIx = value % self.bits

        mask = (1 << bitIx)
        return mask

    def set_value(self, value):
        if value not in self:
            value -= self.from_val
            lineIx = value / self.bits
            mask = self.get_mask(value)

            self.numbers[lineIx] = self.numbers[lineIx] | mask

def main():
    with open('C-small-attempt1.in', 'r') as f_in:
        inp = f_in.readline()

        case_cnt = int(inp)
        
        for caseIx in range(1, case_cnt + 1):
            
            inp = f_in.readline()
            bounds = inp.split()
            floor = int(bounds[0])
            ceil = int(bounds[1])

            nums = numbers(floor,ceil)

            cnt = 0
            ultimate_list = []
            for num in range(floor, ceil):
                num_str = str(num)
                set_list = []
                for i in range(1, len(num_str)):
                    
                    tmp = int(num_str[i:] + num_str[:i])

                    if num not in nums and num < tmp and str(tmp)[0] != '0' and tmp not in set_list and tmp >= floor and tmp <= ceil:
                        if num not in set_list:
                            set_list.append(num)
                        set_list.append(tmp)

                if len(set_list) > 0:
                    old_cnt = cnt
                    cnt += ((len(set_list) * (len(set_list) - 1)) / 2)
                for val in set_list:
                    nums.set_value(val)
            
            with open('C-small-attempt1.out', 'a') as f_out:
                f_out.write('Case #' + str(caseIx) + ': ' + str(cnt) + '\n')

main()

