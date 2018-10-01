#!/usr/bin/python

T = int(raw_input())
for t in range(T):
    N_str = raw_input().strip()
    min_tidy_str = '0' * len(N_str)
    
    for i in range(len(N_str)):
        if int(N_str) < int(min_tidy_str):
            min_tidy_str = str(int(min_tidy_str[:i]) - 1) + ('9' * (len(N_str) - i))
            break
        else:
            min_tidy_str = min_tidy_str[:i] + (N_str[i] * (len(N_str) - i))
    
    min_tidy_str = str(int(min_tidy_str))
    print "Case #%d: %s" % (t + 1, min_tidy_str)