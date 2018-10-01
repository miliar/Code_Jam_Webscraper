def read_input_file(filename = "A-small-attempt1.in"):
    file = open(filename, 'r')
    lines = file.readlines()
    file.close()
    N = int(lines[0])
    cases = []
    for line in lines[1:]:
        cases.append(line)
    return N, cases

N, cases = read_input_file()

mapper = {' ': ' ',
'a': 'y',
'b': 'h',
'c': 'e',
'd': 's',
'e': 'o',
'f': 'c',
'g': 'v',
'h': 'x',
'i': 'd',
'j': 'u',
'k': 'i',
'l': 'g',
'm': 'l',
'n': 'b',
'o': 'k',
'p': 'r',
'q': 'z',
'r': 't',
's': 'n',
't': 'w',
'u': 'j',
'v': 'p',
'w': 'f',
'x': 'm',
'y': 'a',
'z': 'q'}


results = []

for case in cases:
    output_string = ''
    for letter in case:
        if letter in mapper:
            output_string += mapper[letter]
    output_string.strip()
    results.append(output_string)

def create_output(filename = "A_solution.txt"):
    file = open(filename, 'w')
    for i in range(len(cases)):
        print "Case #%d: %s" % (i+1, results[i])
        output = "Case #%d: %s\n" % (i+1, results[i])
        file.write(output)
    file.close()

create_output()

