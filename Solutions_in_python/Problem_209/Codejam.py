def codejam_run(*args, IFS=" ", OFS=" ", I_line_count=1):

    if len(args) > 0:
        r = reader(*args)
        return r.codejam_run

    def codejam_decorator(program):

        num_of_datasets = int(input())

        std_io = []

        if callable(I_line_count):
            for i in range(num_of_datasets):
                first_data_line = input()
                line_count = I_line_count(first_data_line)
                std_io.insert(i, [first_data_line] + [input()
                                                   for _ in range(line_count)])
        else:
            std_io = [[input() for _ in range(I_line_count)]
                                    for __ in range(num_of_datasets)]

        indata = [[line.split(IFS) for line in dataset] for dataset in std_io ]

        if I_line_count == 1:
            indata = [indatum[0] for indatum in indata]

        outdata = [OFS.join(program(*i)) for i in indata]

        for idx, datum in enumerate(outdata, 1):
            print("Case #%i:%s%s" % (idx, OFS, datum))

    return codejam_decorator


class line:
    def __init__(self, times=1, FS=" ", stdtype=int, array_name=None, **kwargs):
        self.times = times
        self.datatypes = kwargs
        self.FS = FS
        self.stdtype = stdtype
        self.array_name = array_name
        self.is_vector = True if times == 1 else False

class reader:
    def __init__(self, *args):
        for arg in args:
            assert(isinstance(arg, line))

        self.lines = args
        self._read()

    def _read(self):
        T = int(input())
        self.in_data = []

        for _ in range(T):
            data = {}

            for line in self.lines:
                data.update(self._readline(line, data))

            self.in_data.append(data)


    def _readline(self, line, data):
        linerepeat = line.times if isinstance(line.times, int)\
                                else data[line.times]

        multi_line_data = []

        for __ in range(linerepeat):
            inp = input().split(line.FS)

            datatypes = (line.stdtype,) * len(inp) if len(line.datatypes) == 0\
                                                   else line.datatypes.values()

            var_names = line.datatypes.keys()

            multi_line_data.append([dt(i) for dt, i in zip(datatypes, inp)])

        if line.array_name != None:
            return {line.array_name: multi_line_data[0] if line.is_vector\
                                                        else multi_line_data}
        else:
            return {*zip(var_names, multi_line_data[0])}

    def codejam_run(self, program):
        for idx, data in enumerate(self.in_data, 1):
            out = program(**data)
            print("Case #%i:%s" % (idx, out))

        return program

