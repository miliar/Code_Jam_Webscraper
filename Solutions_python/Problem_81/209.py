#!/usr/bin/env python
# -*- coding: utf-8 -*-


if __name__ == "__main__":
    f = open("A-large.in")
    T = int(f.readline())
    for t in range(T):
        N = int(f.readline())
        lines = []
        wp = []
        owp = []
        oowp = []
        for n in range(N):
            lines.append(f.readline().strip())
        for n in range(N):
            n0 = lines[n].count('0')
            n1 = lines[n].count('1')
            wp += [1.0 * n1 / (n0 + n1)]
        for n in range(N):
            _owp = []
            for m in range(N):
                if n == m or lines[m][n] == '.': continue
                n0 = (lines[m][0:n]+lines[m][n+1:N]).count('0')
                n1 = (lines[m][0:n]+lines[m][n+1:N]).count('1')
                _owp += [1.0 * n1 / (n0 + n1)]
            owp += [sum(_owp) / len(_owp)]
        for n in range(N):
            _oowp = []
            for m in range(N):
                if lines[m][n] == '.': continue
                _oowp += [owp[m]]
            oowp += [sum(_oowp) / len(_oowp)]
        print "Case #%d:" % (t+1)
        for n in range(N):
            print 0.25 * wp[n] + 0.5 * owp[n] + 0.25 * oowp[n]
        
