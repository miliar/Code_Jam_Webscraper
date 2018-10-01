#!/usr/bin/python3
#
# NOTE: will not work in Python 2.x
#

import re


# main code
if __name__ == '__main__':
    try:
        _word_length, dict_length, _num_cases = map(int, input().split())

        alien_wordlist = []
        for _ in range(dict_length):
            alien_wordlist.append(input().strip())

        alien_dict = '\n'.join(alien_wordlist)

        caseno = 1
        while True:
            wordpat = input().strip()
            wordpat = wordpat.replace('(', '[')
            wordpat = wordpat.replace(')', ']')

            wordre = re.compile(wordpat)

            matchcount = len(wordre.findall(alien_dict))

            print('Case #{}: {}'.format(caseno, matchcount))
            caseno += 1

    except EOFError:
        pass
