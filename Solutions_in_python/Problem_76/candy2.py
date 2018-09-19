'''
Created on May 7, 2011

@author: karnr
'''

from itertools import imap
from operator import mul

def _parse_input(input_file):
    fh = open(input_file)
    num_of_tests = int(fh.readline().strip())
    count = 1
    test_data = dict()
    while (count <= num_of_tests):
        num_of_candy = int(fh.readline().strip())
        candy_values = map(int, fh.readline().strip().split())
        assert len(candy_values) == num_of_candy
        candy_values.sort()
        test_data[count] = candy_values
        count += 1
        
    fh.close()
    return test_data
    
def bitarray(num, length):
    n = map(int, list(bin(num))[2:])
    z = [0 for x in range(length)]
    n_size = len(n)
    for i in range(1, n_size + 1):
        z[-i] = n[-i]
        
    return z    
            
def _execute_test(test_input):
    candy_values = test_input
    num_of_candies = len(candy_values)
    total_iteration = 2 ** num_of_candies - 1
    
    results = list()
    
    for idx in xrange(1, total_iteration):
        sean_candies = [e for e in imap(mul, candy_values, bitarray(idx, num_of_candies))]
        patrick_candies = [e for e in imap(mul, candy_values, 
                                           bitarray(total_iteration - idx, num_of_candies))]
                        
        sean_candies_valued_by_patrick = reduce(lambda x,y: x ^ y, sean_candies)
        patrick_candies_valued_by_patrick = reduce(lambda x,y: x ^ y, patrick_candies)
        
        if (sean_candies_valued_by_patrick != patrick_candies_valued_by_patrick):
            continue
        
        sean_candies_actual_value = sum(sean_candies)
        patrick_candies_actual_value = sum(patrick_candies)
                
        if sean_candies_actual_value < patrick_candies_actual_value:
            continue
        
        results.append((sean_candies_actual_value, sean_candies))
        
    if len(results) > 0:
        return max(results)[0]
    
    return 'NO'

def main():
    test_data_set = _parse_input("test_input")
    num_of_tests = len(test_data_set.keys())
    
    output = open("test_output", "w")
    for test_id in xrange(1, num_of_tests + 1):
        test_data = test_data_set[test_id]
        test_result = _execute_test(test_data)
        output.write("Case #%s: %s\n" % (test_id, test_result))
        
    output.close()

if __name__ == '__main__':
    main()