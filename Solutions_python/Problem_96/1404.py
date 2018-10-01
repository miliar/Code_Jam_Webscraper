#!/usr/bin/python

MAX_SURPRISE = 28
MIN_SCORE = 0 
MIN_SCORE_SURPRISE = 2

def main():
    f = open("b.in")
    for i in xrange(int(f.readline())):
        print "Case #" + str(i+1) + ": " + str(handle_case(f.readline().rstrip()))

def handle_case(line):
    numbers = [int(x) for x in line.split(" ")]
    n = numbers[0]
    s = numbers[1]
    p = numbers[2]
    scores = numbers[3:]
    min_score = max(MIN_SCORE,(p*3)-2)
    min_score_surprise = max(MIN_SCORE_SURPRISE,min_score - 2)
    count = 0
    count_surprise = 0
    for i in xrange(n):
        if scores[i] >= min_score:
            count += 1
        elif MAX_SURPRISE >= scores[i] >= min_score_surprise:
            count_surprise += 1 
    return count + min(count_surprise, s)
        
main()
