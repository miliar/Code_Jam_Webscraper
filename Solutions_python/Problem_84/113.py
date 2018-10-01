'''
Created on May 21, 2011

@author: karnr
'''
def _parse_input(input_file):
    fh = open(input_file)
    num_of_tests = int(fh.readline().strip())
    count = 1
    test_data = dict()
    while (count <= num_of_tests):
        rows, cols = map(int, fh.readline().strip().split())
        idx = 0
        tiles = list()
        while (idx < rows):
            tiles.append(fh.readline().strip().split())
            idx += 1
                        
        test_data[count] = tiles
        count = count + 1
    
    fh.close()
    return test_data

def _execute_test(test_data):
    data = list()
    for l in test_data:
        for t in l:
            data.append(list(t))
    
    rows = len(data)
    cols = len(data[0])
    
    #print (rows, cols, data)
    
    for r in range(rows-1):
        for c in range(cols-1):
            #print (r,c, data[r][c])
            color = data[r][c]
            if color == '.':
                continue
            
            if color == '#':
                if (data[r][c+1] == data[r+1][c] == data[r+1][c+1] == color):
                    data[r][c] = "/"
                    data[r][c+1] = '\\'
                    data[r+1][c] = '\\'
                    data[r+1][c+1] = "/"
    
    
    possible = True
    for r in range(rows):
        for c in range(cols):
            if data[r][c] == '#':
                possible = False
                break
            
    if not possible:
        return 'Impossible'
    
    result = list()
    for l in data:
        result.append("".join(l))
        
    return "\n".join(result)

def main():
    test_data_set = _parse_input("test_input")
    num_of_tests = len(test_data_set.keys())
    output = open("test_output", "w")
    for test_id in xrange(1, num_of_tests + 1):
        test_data = test_data_set[test_id]
        test_result = _execute_test(test_data)
        output.write("Case #%s:\n%s\n" % (test_id, test_result))
        
    output.close()
    
if __name__ == '__main__':
    main()