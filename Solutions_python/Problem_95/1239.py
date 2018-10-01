#!/usr/bin/env python

input_file = 'tongues-small.dat'

google_dict = {
    'y': 'a',
    'n': 'b',
    'f': 'c',
    'i': 'd',
    'c': 'e',
    'w': 'f',
    'l': 'g',
    'b': 'h',
    'k': 'i',
    'u': 'j',
    'o': 'k',
    'm': 'l',
    'x': 'm',
    's': 'n',
    'e': 'o',
    'v': 'p',
    'z': 'q',
    'p': 'r',
    'd': 's',
    'r': 't',
    'j': 'u',
    'g': 'v',
    't': 'w',
    'h': 'x',
    'a': 'y',
    'q': 'z',
    ' ': ' ',
    '\n': ''
}

with open (input_file, 'r') as data_file:
    N_tests = int(data_file.readline())
    for i in range(0,N_tests):
        test_line = data_file.readline()
        
        translated = []
        for char in test_line:
            translated.append(google_dict[char])
        
        case_str = "Case #{0:d}: {1!s}".format(i+1, ''.join(translated))
        print case_str
