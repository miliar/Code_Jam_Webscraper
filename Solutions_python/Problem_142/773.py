#!/usr/bin/python

import sys;

def main():
    T = int(sys.stdin.readline().strip())

    for i in xrange(0, T):
        N = int(sys.stdin.readline().strip())
        strings = []
        for j in xrange(0, N):
            strings.append(sys.stdin.readline().strip())
        ans(N, strings, i+1)


def ans(N, strings, case):
    chars = []
    for i in xrange(0, N):
        chars.append( analyze_str(strings[i]) )

    l = len(chars[0])
    for i in xrange(1, N):
        # check length
        if len(chars[i]) != l:
            print "Case #%d: Fegla Won" % (case)
            return
        # check chars
        for j in xrange(0, l):
            if chars[i][j]['char'] != chars[0][j]['char']:
                print "Case #%d: Fegla Won" % (case)
                return

    nstep = 0
    for j in xrange(0, l):
        nstep += calc_distance(N, chars, j);

    print "Case #%d: %d" % (case, nstep)


def analyze_str(s):
    prv = ''
    ret = []
    for i in xrange(0, len(s)):
        if s[i] == prv:
            ret[-1]["count"] += 1
        else:
            ret.append({"char":s[i], "count":1})
        prv = s[i]
    return ret


def calc_distance(N, chars, j):

    # calc average
    ave = 0
    for i in xrange(0, N):
        ave += chars[i][j]['count']
    ave = float(ave)/N

    # search number of chars nearest to the average
    dist_near = 101
    i_near = -1
    for i in xrange(0, N):
        distance = abs(chars[i][j]['count'] - ave)
        if distance < dist_near:
            dist_near = distance
            i_near    = i

    # calc distances
    ret = 0
    for i in xrange(0, N):
        ret += abs(chars[i][j]['count'] - chars[i_near][j]['count'])
    
    return ret



if __name__ == "__main__":
    main()

