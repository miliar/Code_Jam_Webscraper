from contextlib import ContextDecorator

class Jamfile(ContextDecorator, object):
    def __init__(self, in_name, out_name='out', has_header=True):
        self.__in_name = in_name
        self.__out_name = out_name
        self.__has_header = has_header

    def __enter__(self):
        self.open()
        return self

    def __exit__(self, *exc):
        self.close()
        return exc == None

    def open(self):
        self.__out_file = open(self.__out_name, 'w')
        self.__tc_num = 1
        
        if self.__has_header:
            with open(self.__in_name, 'r') as in_file:
                self.header = in_file.readline()

    def close(self):
        self.__out_file.close()
        del self.__out_file

    def testcases(self):
        with open(self.__in_name) as in_file:
            if self.__has_header:
                in_file.readline()
            for line in in_file:
                yield line

    def write(self, text, tc_num=None, end='\n'):
        if tc_num == None:
            tc_num = self.__tc_num
        self.__out_file.write('Case #' + str(tc_num) + ': ' + str(text) + end)
        self.__tc_num = tc_num + 1
