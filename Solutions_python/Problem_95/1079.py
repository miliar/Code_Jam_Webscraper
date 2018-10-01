def mkdict():
    gs1 = "ejp mysljylc kd kxveddknmc re jsicpdrysi"
    gs2 = "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd"
    gs3 = "de kr kd eoya kw aej tysr re ujdr lkgc jv"
    es1 = "our language is impossible to understand"
    es2 = "there are twenty six factorial possibilities"
    es3 = "so it is okay if you want to just give up"
    gs = gs1 + gs2 + gs3 + "zq"
    es = es1 + es2 + es3 + "qz"
    gdict = {}
    for i in range(0, len(gs)):
        gdict[gs[i]] = es[i]
    #print sorted(set(es))
    return gdict

def main():
    gdict = mkdict()
    #print sorted(gdict)
    line = raw_input()
    cases = int(line)
    for i in range(cases):
        line = raw_input()
        output = map(lambda x: gdict[x], line)
        print "Case #%d: %s" % (i+1, ''.join(output))

if __name__ == "__main__":
    main()
