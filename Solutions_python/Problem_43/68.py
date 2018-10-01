'''
Created on 13 sep 2009

@author: magnus
'''
import sys

class Base(object):
    
    def solve(self, message):
        base = self.get_base(message)
        order = self.get_order(message)
        return self.calculate(message, base, order)
    
    def get_order(self, message):
        mapping = {}
        for symbol in message:
            if not symbol in mapping:
                if len(mapping) == 0:
                    mapping[symbol] = 1
                elif len(mapping) == 1:
                    mapping[symbol] = 0
                else:
                    mapping[symbol] = len(mapping)
        return mapping
                    
    def get_base(self, message):
        unique_symbols = set()
        for symbol in message:
            unique_symbols.add(symbol)
        return max(2,len(unique_symbols))

    def calculate(self, message, base, order):
        value = 0
        index = 0
        for symbol in message[::-1]:
            value = value + order[symbol] * base ** index
            index = index + 1
        return value
    
def get_tests():
    tests = []
    input_file = open(sys.argv[1])
    case_numbers = int(input_file.readline().strip())
    for case_number in range(case_numbers):
        tests.append(input_file.readline().strip())
    return tests
            
if __name__ == '__main__':
    base = Base()
    tests = get_tests()
    index = 1
    for test in tests:
        value = base.solve(test)
        print "Case #" + str(index)+ ": " + str(value)
        index = index +1
        