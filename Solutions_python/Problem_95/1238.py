# -------------------
# about


# solution to code jam 2012 - qualification A 
# usage: python speaking_in_tongues.py
# Python 2.7.2
# 2012-04-14


# -------------------
# figure out the mapping

alphabet = ' abcdefghijklmnopqrstuvwxyz'
mapping_g_to_en = {}

# use hints from description
mapping_g_to_en[' '] = ' '
mapping_g_to_en['y'] = 'a'
mapping_g_to_en['e'] = 'o'
mapping_g_to_en['q'] = 'z'

# use hints from tiny practice
sample_g = []
sample_g += [g for g in 'ejp mysljylc kd kxveddknmc re jsicpdrysi'.split()]
sample_g += [g for g in 'rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd'.split()]
sample_g += [g for g in 'de kr kd eoya kw aej tysr re ujdr lkgc jv'.split()]

sample_en = []
sample_en += [en for en in 'our language is impossible to understand'.split()]
sample_en += [en for en in 'there are twenty six factorial possibilities'.split()]
sample_en += [en for en in 'so it is okay if you want to just give up'.split()]

# figure out the mapping from samples until mapping complete or out of samples
for g,en in zip(sample_g,sample_en):
    assert len(g) == len(en), 'should be one letter to one letter mapping'
    alphabet_size = len(alphabet)
    if len(mapping_g_to_en.keys()) == alphabet_size: # all mappings figured out
        break
    if len(mapping_g_to_en.keys()) == alphabet_size - 1: # figure out the last mapping using onto constraint
        last_g_letter_found = False
        last_en_letter_found = False
        for letter in alphabet:
            if letter not in mapping_g_to_en.keys():
                last_g_letter = letter
                last_g_letter_found = True
            if letter not in mapping_g_to_en.values():
                last_en_letter = letter
                last_en_letter_found = True
            if last_g_letter_found and last_en_letter_found:
                break
        mapping_g_to_en[last_g_letter] = last_en_letter
    for i in range(len(g)): # collect mapping from samples
        g_letter = g[i]
        # no saturation check, in worst case waste 99 (i.e., 100-1) checks
        if g_letter not in mapping_g_to_en:
            mapping_g_to_en[g_letter] = en[i]
assert set(mapping_g_to_en.keys()) == set(mapping_g_to_en.values()), 'should be onto mapping'


# -------------------
# translate a line from Googlerese to English


def translate_g_en(source):
    target = ''
    for i in range(0,len(source)):
        target += mapping_g_to_en[source[i]]
    return target


# -------------------
# solve a task


def solve(f_name_in, f_name_out):
    f_in = open(f_name_in, 'r')
    num_tests = int(f_in.readline().split()[0])
    f_out = open(f_name_out, 'w')
    for i in range(0,num_tests):
        case_num = i+1
        source = f_in.readline()[:-1] # [:-1] trims end of line character
        target = translate_g_en(source)
        result = 'Case #%d: %s\n' %(case_num, target)
        f_out.write(result)
    f_in.close()
    f_out.close()


# -------------------
# solving

solve('A-small-attempt0.in', 'A-small-attempt0.out')
