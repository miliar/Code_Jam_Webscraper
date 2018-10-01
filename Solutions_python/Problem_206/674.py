#! /usr/bin/env python3

import os
import os.path
import argparse
from pprint import pprint

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("filename", help='Filename')

    args = parser.parse_args()

    outputfile = os.path.splitext(args.filename)[0] + ".out"

    with open(args.filename, 'r') as f:
        with open(outputfile, 'w+') as fout:
            num_tests = int(f.readline().strip())
            for testcase in range(1,num_tests+1):
                destination, num_horses = [int(x) for x in f.readline().split(" ")]
                max_time = 0
                print("Case #{} Input: dest={}, {} horses".format(testcase, destination, num_horses))
                for i in range(num_horses):
                    current, speed = [int(x) for x in f.readline().split(" ")]
                    current_time = (destination - current) / speed
                    max_time = max(current_time, max_time)
                speed = destination / max_time
                print("Output: {:.6f} (max_time = {} hours)".format(speed, max_time))
                fout.write("Case #{}: {:.6f}\n".format(testcase, speed))


