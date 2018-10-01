#!/usr/bin/env python
# -*- coding: utf-8 -*-

def solve(N,vals):
    ans_first = 0
    for i in range(len(vals)):
        if i==0:
			continue
        else:
			prev = vals[i-1]
			cur = vals[i]
			if prev > cur:
				ans_first += prev - cur
    
    rates=[0]
    ans_second = 0
    for i in range(len(vals)):
        if i==0:
            continue
        else:
            prev = vals[i-1]
            cur = vals[i]
            if prev > cur:
                diff = prev-cur
                #tmp_rate = (diff+9)/10
                tmp_rate=diff
                #tmp_rate = float(diff) / 10.0
                rates.append(tmp_rate)
    rate = max(rates)
    for i in range(len(vals)):
        if i==0:
            continue
        else:
            prev = vals[i-1]
            cur = vals[i]
            if rate>0:
                #diff=prev
                #ans_second+=min((diff+rate-1)/rate * rate,10*rate)
                ans_second+=min(prev,rate)
    
    return str(ans_first)+" "+str(ans_second)

if __name__ == "__main__":
    testcases = input()
     
    for caseNr in xrange(1, testcases+1):
        N=int(raw_input().strip())
        vals=[int(digit) for digit in raw_input().strip().split()]
        print("Case #%i: %s" % (caseNr, solve(N,vals)))
