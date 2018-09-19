import pprint

out_fd = open('a.out', 'w')

mapping = {
 ' ': ' ', 
 '\n': '\n',
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
 'z': 'q',
}

# Construct the rest of the mapping table from samples
# NOT necessary anymore since I ran it once and encoded the mapping above
"""
sample_out_fd = open('a_sample.out')
with open('a_sample.in') as sample_in_fd:
    n = int(sample_in_fd.readline())
    for googlerese, english in zip(sample_in_fd, sample_out_fd):
        googlerese = googlerese.strip() # get rid of newline
        english = ' '.join(english.split()[2:])  # get rid of Case #n:
        if not len(googlerese) == len(english):
            print "length not equal {0} vs {1}: {2} TO {3}".format(
                len(googlerese), len(english),
                googlerese, english)
        for g, e in zip(googlerese, english):
            mapping[g] = e
sample_out_fd.close()
pprint.pprint(mapping)
"""

with open('a.in') as in_fd:
    n = int(in_fd.readline())
    for i, line in enumerate(in_fd):
        out_fd.write('Case #{0}: '.format(i + 1))
        for c in line:
            out_fd.write('{0}'.format(mapping.get(c, '!')))
out_fd.close()
