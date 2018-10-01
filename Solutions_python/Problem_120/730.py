#!/usr/bin/env python2.7

# Standard libs
import sys

# Constants
USAGE = "python %s INPUT_FILE" % (sys.argv[0])

def main(argv):
    if len(argv) != 2:
        raise Exception("Invalid arguments! Usage: %s" % (USAGE))

    input_filename = argv[1]

    with open(input_filename, "r") as input_file:
        # Read in the number of test cases
        try:
            num_test_cases = int(input_file.readline().strip())
        except:
            raise Exception("Invalid input file")

        # Determine the maximum number of black rings around the bullseye for
        # each test case
        for test_case_number in range(1, num_test_cases + 1):
            initial_radius, paint_volume = map(int, input_file.readline().strip().split())
            max_black_rings = get_max_black_rings(initial_radius, paint_volume)
            print "Case #%d: %d" % (test_case_number, max_black_rings)

def get_max_black_rings(initial_radius, paint_volume):
    ring_count = 0

    # Paint required for first ring
    paint_for_ring = (initial_radius + 1)**2 - initial_radius**2

    paint_volume -= paint_for_ring

    while paint_volume >= 0:
        ring_count += 1

        # The paint required for subsequent rings can be found by adding the
        # difference between alternating squares
        paint_for_ring += 4

        paint_volume -= paint_for_ring

    return ring_count

if __name__ == "__main__":
    main(sys.argv)
