#!/usr/bin/env python

def no_conflict(d1, d2):
    for k in d2:
        if d1.has_key(k):
            if d1[k] != d2[k]:
                return False
    return True

def googlerese_dict(lang_mappings):
    mapping = {}
    for gog, eng in lang_mappings.items():
        infered_mapping = dict(zip(gog, eng))
        assert no_conflict(mapping, infered_mapping)
        mapping.update(infered_mapping)
    return mapping

trans = googlerese_dict({
        "y" : "a",
        "e" : "o",
        "z" : "q",
        "q" : "z",
        "ejp mysljylc kd kxveddknmc re jsicpdrysi" : "our language is impossible to understand",
        "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd" : "there are twenty six factorial possibilities",
        "de kr kd eoya kw aej tysr re ujdr lkgc jv" : "so it is okay if you want to just give up"}) 

rev = dict((v,k) for (k,v) in trans.items())

def translate_g2e(s):
    return "".join(trans[e] for e in s)
def translate_e2g(s):
    return "".join(rev[e] for e in s)

if __name__ == '__main__':
    import sys
    with open(sys.argv[1]) as f:
        lines = f.readlines()[1:]
    translated = [translate_g2e(l.strip()) for l in  lines]
    for i,t in enumerate(translated):
        print "Case #{}: {}".format(i+1,t)
