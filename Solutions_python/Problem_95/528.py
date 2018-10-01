
from string import ascii_lowercase

S = ('our language is impossible to understand'
     'there are twenty six factorial possibilities'
     'so it is okay if you want to just give up'
     'zq')

G = ('ejp mysljylc kd kxveddknmc re jsicpdrysi'
     'rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd'
     'de kr kd eoya kw aej tysr re ujdr lkgc jv'
     'qz')

def main():

    m = dict()

    for (s,g) in zip(S,G):
        m[g] = s

    print ', '.join("'%s': '%s'" % (g, m[g]) for g in ascii_lowercase)

if __name__ == '__main__':
    main()
