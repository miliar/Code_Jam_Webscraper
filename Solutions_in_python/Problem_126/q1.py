'''
Created on Apr 13, 2012

@author: karnr
'''
vowels = ['a', 'e', 'i', 'o', 'u']

def match_consonants(s):
    for a in s:
        if a in vowels:
            return False
        
    return True

def _execute_test(test_input):
    print test_input
    (name, n) = test_input
    n = int(n)
    
    sub_strings = []
    for i in range(0, len(name) - n + 1):
        a = i
        b = i + n
        s = name[a:b]
        match = match_consonants(s)
        if match:
            p = a + 1
            before = zip(range(p),[b] * p)
            
            q = range(b + 1, len(name) + 1)
            after = zip([a] * len(q), q)
            
            joined = []
            for x in range(p):
                for y in q:
                    joined.append((x,y))
            sub_strings.extend(before)
            sub_strings.extend(after)
            sub_strings.extend(joined)
            
            #print s, sub_strings
        
    ans = set(sub_strings)
    return len(ans)

def _parse_input(input_file):
    fh = open(input_file)
    num_of_tests = int(fh.readline().strip())
    count = 1
    test_data = dict()
    while (count <= num_of_tests):
        test_data[count] = fh.readline().strip().split()
        count += 1
        
    fh.close()
    
    return test_data

def main():
    test_data_set = _parse_input("test_input")
    num_of_tests = len(test_data_set.keys())
    
    output = open("test_output", "w")
    for test_id in xrange(1, num_of_tests + 1):
        test_data = test_data_set[test_id]
        test_result = _execute_test(test_data)
        print "Case #%s: %s\n" % (test_id, test_result)
        output.write("Case #%s: %s\n" % (test_id, test_result))
        
    output.close()
    
if __name__ == '__main__':
    main()