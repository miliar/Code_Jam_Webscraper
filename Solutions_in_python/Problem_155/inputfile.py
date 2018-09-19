

class InputFile(object):
    def __init__(self, input_filename, lines_per_test, output_filename):
        self._input_filename = input_filename
        self._test_num = 0
        self._lines_per_test = lines_per_test
        self._results = []
        self._output_filename = output_filename
        
    def get_tests(self):
        with open(self._input_filename, 'r') as input:
            self._test_num = int(input.readline())
            
            while True:
                next_test = []
                line = input.readline()
                if (line == ""):
                    next_test = None
                    input.close()
                    break
                else:
                    next_test.append(line)
                    for i in range(self._lines_per_test-1):
                        next_test.append(input.readline())
            
                    yield next_test
                    
        
    def store_result(self, result):
        self._results.append(result)
        
    def save_file(self):
        contents = ""
        count = 1
        for result in self._results:
            contents += "Case #{}: {}\n".format(count, result)
            count += 1
            
        with open(self._output_filename, 'w') as file:
            file.write(contents)
            file.close()
            