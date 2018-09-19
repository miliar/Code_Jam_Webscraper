class ProblemManager:

    def __init__(self, handler_func, infile, outfile, num_lines):

        """
        @param input_file_name: (str)
        @param input_lines_per_problem: (int) google input files have a consistent number of lines that
            define the input to each problem.
        """
        self.input_file_name = infile
        self.output_file_name = outfile
        self.input_lines_per_problem = num_lines
        self.handler_func = handler_func
        self.parse_int = True

    def run(self):
        parsed_input_data = self._parse_input_file()
        if self.output_file_name:
            with open(self.output_file_name, 'w'):
                pass
            f = open(self.output_file_name, 'a')
        else:
            f = None

        for i, problem in enumerate(parsed_input_data):
            result = self.handler_func(problem)
            self._output(f, i + 1, result)

        if f:
            f.close()

    def _output(self, f, case, text):
        """
        Given a case number and some output, print that output to data.out
        """
        if f:
            f.write("Case #%s: %s\n"  % (case, text))
        else:
            print "Case #%s: %s\n"  % (case, text),

    def _parse_input_file(self):
        """
        Parses the input file such that:
        (a) the first line is removed
        (b) each line of input is a list of 1+ elements that are the space-deliniated string of that line
        (c) a list of such lists is returned, where each element of the final list is the split lines
            of the inputs (as determined by self.input_lines_per_problem)
        """
        problems = []
        with open(self.input_file_name) as f:
            number_test_cases = int(f.readline().strip())
            for _ in range(number_test_cases):
                problems.append(self._parse_problem(f))
        return problems

    def _parse_problem(self, f):
        if self.input_lines_per_problem == 1:
            return self._parse_line(f)

        lines = []
        for i in range(self.input_lines_per_problem):
            line = self._parse_line(f)
            lines.append(line)
        return lines

    def _parse_line(self, f):
        line = f.readline().strip()
        if not line:
            raise Exception("Problem ran out of input before it was over")
        result = line.split(" ")
        return map(self._try_to_parse_int, result)

    def _try_to_parse_int(self, item):
        if not self.parse_int:
            return item
        try:
            return int(item)
        except Exception:
            return item
