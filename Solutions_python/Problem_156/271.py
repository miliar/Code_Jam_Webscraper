
#!/usr/bin/python

import sys
import os
from collections import defaultdict, Counter

results = dict()

"""
def recur_pan(pancake_count, extra_minutes, last_max_minutes):
    max_minutes = max(pancake_count) + extra_minutes
    if max_minutes >= last_max_minutes: return max_minutes
    last_max_minutes = max_minutes
    if max_minutes <= 3: return max_minutes
    if max_minutes <= 5 and pancake_count.count(max_minutes) >= 2: return max_minutes
    if max_minutes <= 7 and pancake_count.count(max_minutes) >= 3: return max_minutes
    new_pancake_count = pancake_count + [0]
    for i in xrange(len(pancake_count)):
        for amount in xrange(2,(pancake_count[i]+2)/2):
            new_pancake_count[i] -= amount
            new_pancake_count[len(pancake_count)] = amount
            recur_max = recur_pan(new_pancake_count, extra_minutes + 1, last_max_minutes)
            max_minutes = min(max_minutes, recur_max)
            #for k in xrange(extra_minutes+1):
            #    sys.stdout.write(" -- ")
            #print(new_pancake_count, extra_minutes + 1, recur_max)
            new_pancake_count[i] += amount
            new_pancake_count[len(pancake_count)] = 0
    return max_minutes
"""

def recur_pan(pancake_count, extra_minutes):
    max_pancake = max(pancake_count)
    max_same_counts = pancake_count.count(max_pancake)
    max_minutes = max_pancake + extra_minutes
    if max_minutes <= 3: return max_minutes
    #if max_minutes <= 5 and max_num >= 2: return max_minutes
    #if max_minutes <= 7 and max_num >= 3: return max_minutes

    for amount in xrange(2,(max_pancake+2)/2):
        new_pancake_count = pancake_count + [amount]*max_same_counts
        for i in xrange(len(pancake_count)):
            if new_pancake_count[i] == max_pancake:
                new_pancake_count[i] -= amount
        recur_max = recur_pan(new_pancake_count, extra_minutes + max_same_counts)
        max_minutes = min(max_minutes, recur_max)
        #for k in xrange(extra_minutes+1):
        #    sys.stdout.write(" -- ")
        #print(new_pancake_count, extra_minutes + max_same_counts, recur_max)
    return max_minutes
"""

    for i in xrange(len(pancake_count)):
        for amount in xrange(2,(pancake_count[i]+2)/2):
            new_pancake_count[i] -= amount
            new_pancake_count[len(pancake_count)] = amount
            recur_max = recur_pan(new_pancake_count, extra_minutes + 1, last_max_minutes)
            max_minutes = min(max_minutes, recur_max)
            #for k in xrange(extra_minutes+1):
            #    sys.stdout.write(" -- ")
            #print(new_pancake_count, extra_minutes + 1, recur_max)
            new_pancake_count[i] += amount
            new_pancake_count[len(pancake_count)] = 0
    return max_minutes
"""

def inf_pancake(input_filename):
    input_file = open(input_filename, "r")
    num_test_cases = int(input_file.readline().strip())
    for i in xrange(num_test_cases):
        num_diners = int(input_file.readline().strip())
        pancake_count = map(int, input_file.readline().strip().split())
        #total_pancakes = sum(pancake_count)
        #pancake_count = [i]*3
        #print(pancake_count)
        num_minutes = recur_pan(pancake_count, 0)
        print(pancake_count, num_minutes)
        #if num_minutes < i:
        #    break
        #if pancake_count == [3,9,2,2]: break
        """
        reach_optimal = False
        old_max_minutes = max(pancake_count)
        print(pancake_count)
        while not reach_optimal:
            sys.stdout.write(" -- ")
            print(pancake_count)
            max_index = pancake_count.index(old_max_minutes)
            pancake_count[max_index] -= old_max_minutes/2
            pancake_count.append(old_max_minutes/2)
            extra_minutes += 1
            new_max_minutes = max(pancake_count)
            if extra_minutes + new_max_minutes >= old_max_minutes:
                num_minutes = old_max_minutes + extra_minutes - 1
                reach_optimal = True
            old_max_minutes = new_max_minutes
        sys.stdout.write(" -- ")
        print(num_minutes)
        """

        """
        shy_count = [int(c) for c in shy_count_str]
        min_friends = 0
        total_standing = 0
        #print(max_shy_str, shy_count)
        for j in xrange(int(max_shy_str)):
            total_standing += shy_count[j]
            #print("   "+str((total_standing, j+1, min_friends)))
            if total_standing < j+1:
                min_friends += j+1 - total_standing
                total_standing = j+1
        """

        results[i+1] = num_minutes
    input_file.close()




def write_output():
    output_file = open("output.txt", "w")
    for k,v in results.iteritems():
        output_file.write("Case #"+str(k)+": "+str(v)+"\n")
    output_file.close()


if __name__ == "__main__":
    input_filename = sys.argv[1]
    inf_pancake(input_filename)
    write_output()

#
