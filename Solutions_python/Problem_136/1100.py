#!/usr/bin/env python3
import sys

def solve(C,F,X):
    
    cookies_rate = 2
    total_time = 0.0
    while(True):
        # buy or not?
        
        farm_time = C/cookies_rate
        win_time = X / cookies_rate
        next_win_time = X / ( cookies_rate + F)
        if (next_win_time + farm_time ) > win_time:
#            print(win_time)
            return total_time + win_time
        else:
            cookies_rate += F
            total_time += farm_time
#            print(farm_time)
            


def main(filename):
    with open(filename, 'r') as f:
        testcases = int(f.readline())
        for case_num in range(testcases):
            C,F,X = [float(i) for i in f.readline().split()]

            print("Case #{0}: {1:.7f}".format(case_num + 1, solve(C,F,X)))

if __name__ == '__main__':
    if len(sys.argv) > 1:
        main(sys.argv[1])
