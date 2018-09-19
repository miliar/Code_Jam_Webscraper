# Codejam reader module

def read_string(f):
    return f.readline().strip()

def read_int(f):
    return int(read_string(f))

def read_string_list(f, delim = ' '):
    return read_string(f).split(delim)

def read_int_list(f, delim = ' '):
    return list(map(int, read_string_list(f, delim)))

def read_string_matrix(f, n, delim = ' '):
    return [read_string_list(f, delim) for i in range(n)]

def read_int_matrix(f, n, delim = ' '):
    return [read_int_list(f, delim) for i in range(n)]

def write_file(f, d):
    f.write('Case #{casenumber}: {caseoutput}\n'.format(**d))

def solve(filename, read_file, solver, write_file = write_file):
    filein, fileout = filename + '.in', filename + '.out'
    with open(filein, 'r') as fin:
        with open(fileout, 'w') as fout:
            num = read_int(fin)
            for i in range(num):
                case = read_file(fin)
                result = solver(case)
                write_file(fout, {'casenumber': i+1, 'caseoutput': result})
