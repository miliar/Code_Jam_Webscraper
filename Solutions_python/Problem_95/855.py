IN = ['ejp mysljylc kd kxveddknmc re jsicpdrysi',
      'rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd',
      'de kr kd eoya kw aej tysr re ujdr lkgc jv']
OUT = ['our language is impossible to understand',
       'there are twenty six factorial possibilities',
       'so it is okay if you want to just give up']

codebook = {}

def init_codebook():
    for i in range(len(IN)):
        tin = IN[i]
        tout = OUT[i]
        for j in range(len(tin)):
            cin = tin[j]
            cout = tout[j]
            if cin != ' ':
                if not cin in codebook.keys():
                    codebook[cin] = cout
    codebook['z'] = 'q'
    codebook['q'] = 'z'

def translate(sin):
    sout = ''
    for c in sin:
        if c not in codebook.keys():
            sout += c
        else:
            sout += codebook[c]
    return sout

def main():
    fr = open('in.txt')
    fw = open('out.txt', 'w+')
    n = int(fr.readline())
    for i in range(1, n+1):
        line = fr.readline()
        fw.write('Case #%d: %s'%(i, translate(line)))
    fr.close()
    fw.close()
if __name__ == '__main__':
    init_codebook()
    main()
