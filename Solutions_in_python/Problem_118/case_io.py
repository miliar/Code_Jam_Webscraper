import argparse

class CaseIO():
    """read and write codejam cases"""
    def __init__(self, in_file, out_file, lines_per_case = 1, empty_line_casedelim = True):
        """
        init with 
            input file name
            output file name
            optional : number of lines per case (def 1)
        """
        self.input = in_file
        self.output = out_file
        self.delim_lines = empty_line_casedelim
        # truncate file
        open(self.output,"w").close()
        self.write_cursor = 1
        self.case_length = lines_per_case
        
    def cases(self):
        """
        generate a list of lines per case
        """
        with open(self.input, "r") as source:
            case_count = int(source.readline())
            for i in range(case_count):
                case_lines = ""
                for j in range(self.case_length):
                    case_lines += source.readline()
                yield case_lines.splitlines()
                if self.delim_lines:
                    source.readline()
        
    def write(self, answer):
        """
        write the answer to current case to set output file
        """
        with open(self.output, "ab") as sink:
            nl = "\n" if self.write_cursor > 1 else ""
            text = "{}Case #{:d}: {}".format(nl, self.write_cursor, answer)
            sink.write(bytes(text,"utf-8"))
            self.write_cursor += 1
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('input')
    parser.add_argument('output', nargs = "?", default = "codejam.out")
    args = parser.parse_args()
    io = CaseIO(args.input, args.output, 2)
    print([case for case in io.cases()])
    io.write("first")
    io.write("second")