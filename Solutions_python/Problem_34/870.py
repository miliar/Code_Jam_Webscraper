def tokenize(inp):
    matches = re.findall(r'(\(.*?\)|[a-z])', inp)
    matches = [re.sub(r'[\(\)]', '', match) for match in matches]
    return matches

mz = 0
for pat in pats:
    pat = pat.replace('(', '[')
    pat = pat.replace(')', ']')
    for word in words:
        m = re.findall(pat, word)
        mz += len(m)
    print '%s: %d' % (pat, mz)
    mz = 0
