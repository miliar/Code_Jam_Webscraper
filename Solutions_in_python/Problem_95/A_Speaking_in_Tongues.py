'''
Created on Apr 14, 2012

@author: moemen
'''
def debug(*args):
    print " ".join(str(arg) for arg in args)

def memoizing(func):
    """Function decorator to cache a function's output."""
    memos = dict()
    def memoize(*args):
        if args in memos:
            return memos[args]
        res = func(*args)
        memos[args] = res
        return res
    return memoize


def draw_map(s_in, s_out):
    d = {}
    for i, j in zip(list(s_in), list(s_out)):
        if i == " " and j == " ":
            continue
        elif i == " " or j == " ":
            debug("i: ", i, "\nj: ", j)
        d[i] = j
    d['z'] = 'q'
    d['q'] = 'z'
    return d

def process_file(fin, fout):
    sample_in = "ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv"
    sample_out = "our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up"
    map_dic = draw_map(sample_in, sample_out)
    
    lines = int(fin.readline())
    Googlerese = [fin.readline() for i in range(lines)]
    out_str = []
    for line in Googlerese:
        out_line = ""
        for car in line.strip('\n'):
            if car == " ":
                out_line += " "
                continue
            out_line += map_dic[car]
        out_str.append(out_line)
    for x, s in enumerate(out_str):
        fout.write("Case #{0}: {1}\n".format(x + 1, s))
    

if __name__ == '__main__':
    from sys import argv
    process_file(open(argv[1]), open(argv[1].replace("in", "out"), "w"))
    #process_file(1, 2)
