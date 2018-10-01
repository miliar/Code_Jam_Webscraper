'''Hmm, let's try a maketrans'''

import string


googlese_table = string.maketrans(
    'ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv y qee z',
    'our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up a zoo q')

if __name__ == '__main__':
    N = int(raw_input())
    for i in range(N):
        print('Case #{num}: {answer}'.format(
                num=i+1,
                answer=raw_input().translate(googlese_table)
                ))
        
