#!/usr/bin/env pypy

# IN_FILE = 'sample.in'
# IN_FILE = 'D-small-attempt0.in'
IN_FILE = 'D-large.in'
fp = open(IN_FILE, 'r')

NUM_TESTS = int(fp.readline())
TESTS = []
for i in range(NUM_TESTS):
    num_weights = int(fp.readline())
    nao = [float(x) for x in fp.readline().strip().split(' ')]
    ken = [float(x) for x in fp.readline().strip().split(' ')]
    TESTS.append({
        'nao': tuple(nao),
        'ken': tuple(ken)
    })
fp.close()

# from pprint import pprint
# pprint(TESTS)
# print


def deceitful_war(nao, ken):
    if len(nao) == 0:
        return 0
    if nao[0] > ken[0]:
        return 1 + deceitful_war(nao[1:], ken[1:])
    else:
        return deceitful_war(nao[1:], ken[:-1])


def normal_war(nao, ken):
    if len(nao) == 0:
        return 0
    if nao[-1] > ken[-1]:
        return 1 + normal_war(nao[:-1], ken[1:])
    else:
        return normal_war(nao[:-1], ken[:-1])


for i in range(NUM_TESTS):
    test = TESTS[i]
    nao = sorted(test['nao'])
    ken = sorted(test['ken'])
    dec_res = deceitful_war(nao, ken)
    nor_res = normal_war(nao, ken)
    print 'Case #%d:' % (i + 1),
    print dec_res, nor_res
