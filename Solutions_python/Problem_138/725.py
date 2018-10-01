# -*- coding: utf-8 -*-
# This library is available online and free to use:
# https://github.com/yanatan16/pycodejam
import bisect

from codejam.parsers import iter_parser


def solve(*lines):
    # print lines
    n, N, K = lines
    N.sort()
    K.sort()
    N_deceitful_war = N[:]
    K_war = K[:]
    deceitful_war = n
    war = 0
    for i in xrange(n):
        # print
        # print N
        # print K
        # print 'N[i]', N[i]
        # print 'K[i]', K[i]
        # print 'K[-i - 1]', K[-i - 1]
        if K_war:
            j = bisect.bisect_left(K_war, N[i])
            K_war = K_war[j + 1:]
            war += j
        if N_deceitful_war:
            k = bisect.bisect_left(N_deceitful_war, K[i])
            N_deceitful_war = N_deceitful_war[k + 1:]
            deceitful_war -= k
        # print deceitful_war
        # print war
        # import ipdb; ipdb.set_trace()
    return '{} {}'.format(deceitful_war, war)


@iter_parser
def parse(nxtline):
    n = int(nxtline())
    yield n
    for _ in xrange(2):
        yield map(float, nxtline().split())


if __name__ == "__main__":
    from codejam import CodeJam
    CodeJam(parse, solve).main()
