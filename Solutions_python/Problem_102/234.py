#! /usr/bin/env python

# usage: python template.py <file.in >file.out

T = int(raw_input())
for case in xrange(1, T+1):
    line = map(int, raw_input().split(' '))
    N, judge_scores = line[0], line[1:]
    X = sum(judge_scores)
    # takes out everyone in the "gone" pool
    needed_scores = [score if score > 2.*X/N else 0 for score in judge_scores]
    nns = [1 if score > 2.*X/N else 0 for score in judge_scores]
    top, bottom = 2.*X-sum(needed_scores), N - sum(nns)
    needed_score = top/bottom
    for i in xrange(N):
        if needed_scores[i] == 0:
            needed_scores[i] = needed_score
    for i in xrange(N):
        needed_scores[i] = needed_scores[i] - judge_scores[i]
    # needed_scores = [(X/float(N)-score)*200/X for score in judge_scores]
    # needed_scores = map(lambda x: max(x, 0), needed_scores)
    needed_scores = [100*n/X for n in needed_scores]
    ans = ' '.join(map(str,needed_scores))
    print "Case #%s: %s" %(case, ans)
