import sys, itertools, string
cases = int(sys.stdin.readline())
case = 0

DEBUG=False

mapping = {'y': 'a', 'e': 'o', 'q': 'z'}

inputs = """
ejp mysljylc kd kxveddknmc re jsicpdrysi
rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd
de kr kd eoya kw aej tysr re ujdr lkgc jv
"""

outputs = """
Case #1: our language is impossible to understand
Case #2: there are twenty six factorial possibilities
Case #3: so it is okay if you want to just give up
"""

for _input, _output in zip(inputs.strip().splitlines(), outputs.strip().splitlines()):
    _i = _input.strip()
    _o = _output[_output.index(":")+1:].strip()
    
    mapping.update(zip(_i, _o))

mapping_in, mapping_out = set(mapping.keys()), set(mapping.values())

mapping[(set(string.ascii_lowercase) - set(mapping_in)).pop()] = (set(string.ascii_lowercase) - set(mapping_out)).pop()

while case < cases:

    print("Case #%d:" % (case+1), end=" ")
    case += 1

    print(''.join(mapping[l] for l in sys.stdin.readline().strip()))
        

