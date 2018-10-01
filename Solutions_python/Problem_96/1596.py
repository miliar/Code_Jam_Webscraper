#! /usr/bin/env python
# -*- coding: utf-8 -*-

import sys


def make_scores(ti):
    scores = [ti / 3] * 3
    mod = ti % 3
    if mod:
        for index in range(mod):
            scores[-index - 1] += 1
    return scores


def make_surprise(scores):
    surprise = scores[:]
    surprise[-1] += 1
    surprise[-2] -= 1
    if surprise[0] > surprise[1]:
        surprise[0], surprise[1] = surprise[1], surprise[0]
    bad_surprise = surprise[-1] > 10 or surprise[0] < 0
    bad_surprise |= (surprise[-1] - surprise[0] != 2)
    if bad_surprise:
        return (False, None)
    return (True, surprise)


def filter_posible_scores(p, scores):
    accept_scores = lambda scores: scores[-1] + 1 >= p
    key = lambda scores: scores[0]
    return sorted(filter(accept_scores, scores), key=key)


def apply_surprise_making(S, scores):
    if not S:
        return scores
    for index in xrange(len(scores)):
        result, surprise = make_surprise(scores[index])
        if result:
            scores[index] = surprise
            S -= 1
            if not S:
                break
    return scores


def filter_good_scores(p, scores):
    accept_scores = lambda scores: scores[-1] >= p 
    return filter(accept_scores, scores)


if __name__ == '__main__':
    count = int(raw_input())

    for index in xrange(count):
        data = map(int, raw_input().split())
        N, S, p = data[:3]
        ti = data[3:]

        scores = [make_scores(maximal) for maximal in ti]
        posible = filter_posible_scores(p, scores)
        surprises = apply_surprise_making(S, posible)
        good = filter_good_scores(p, surprises)

        print 'Case #%d: %d' % (index + 1, len(good)) # , '>>', S, p, scores, good

    sys.exit()
