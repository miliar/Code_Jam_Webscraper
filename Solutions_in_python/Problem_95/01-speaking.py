import sys

if not len(sys.argv) == 3:
    exit("""Wrong usage parameters supplied!
    
    Usage:
    %s input output""" % __file__
    )

from itertools import izip

alphabet = set(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
                'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                'u', 'v', 'w', 'x', 'y', 'z'])

set_inp = """our language is impossible to understand
there are twenty six factorial possibilities
so it is okay if you want to just give up"""

set_sol = """ejp mysljylc kd kxveddknmc re jsicpdrysi
rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd
de kr kd eoya kw aej tysr re ujdr lkgc jv"""

g_dict = {}

for ic, oc in izip(set_sol, set_inp):
    if ic in alphabet:
        g_dict[ic] = oc

dicts_var = [
    {'q': 'z', 'z': 'q'},
    {'z': 'z', 'q': 'q'}
]

def translate(s):
    svars = []
    for d in dicts_var:
        parts = []
        for c in s:
            parts.append(g_dict.get(c) or d[c] if c in alphabet else c)
        svars.append(''.join(parts))
    return svars


def main(input_filename, output_filename):
    
    input_f = open(input_filename, "r")
    outputs = [open(output_filename + str(i), "w") for i, d in enumerate(dicts_var)]
    
    try:
        TEST_CASES_NUM = int(input_f.readline())
        
        for test_case_i in xrange(TEST_CASES_NUM):
            
            for i, s in enumerate(translate(input_f.readline().strip())):
                outputs[i].write("Case #%d: %s\n" % (test_case_i + 1, s))
            
    finally:
        input_f.close()
        for output_f in outputs:
            output_f.close()


main(sys.argv[1], sys.argv[2])
