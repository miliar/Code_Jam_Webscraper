#! /usr/bin/env python
# coding:utf-8

maps = {' ': ' ',
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
                         'r': 't',
                          's': 'n',
                           't': 'w',
                            'u': 'j',
                             'v': 'p',
                              'w': 'f',
                               'x': 'm',
                                'y': 'a',
                                'z': 'q',
                                'q': 'z',}

def main():
    s = raw_input()
    n = int(s)
    dt = []
    for i in xrange(n):
        dt.append(raw_input())
    for n, line in enumerate(dt):
        print "Case #"+ str(n+1) + ": "+"".join([maps[i] for i in line])

if __name__ == "__main__":
    main()
