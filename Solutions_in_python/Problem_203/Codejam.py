def codejam_run(IFS=" ", OFS=" ", I_line_count=1):
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
