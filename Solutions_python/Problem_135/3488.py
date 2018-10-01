__author__ = 'ivandasch'
import sys, os

def read_data(filename):
    samples = []
    with open(filename, 'r') as data_file:
        samples_len = int(data_file.readline())
        for x in range(0,samples_len):
            take_one = int(data_file.readline())
            hand_one = []
            for i in range(0,4):
                hand_one.append(set(int(x) for x in data_file.readline().split()))
            take_two = int(data_file.readline())
            hand_two = []
            for i in range(0,4):
                hand_two.append(set(int(x) for x in data_file.readline().split()))
            samples.append({
                "take_one": take_one,
                "hand_one": hand_one,
                "take_two": take_two,
                "hand_two": hand_two
            })
    return samples

def solve(data):
    for i,p in enumerate(data):
        to_i = p["take_one"]
        tt_i = p["take_two"]
        result =  p["hand_one"][to_i-1] & p["hand_two"][tt_i-1]
        if len(result) == 1:
            print "case #%s: %s" % (str(i+1), str(list(result)[0]))
        elif len(result) > 1:
            print "case #%s: Bad magician!" % str(i+1)
        else:
            print "case #%s: Volunteer cheated!" % str(i+1)

data = read_data(sys.argv[1])
solve(data)

