#! /usr/bin/env python

from optparse import OptionParser
import re
import sys

INFO_REGEX = re.compile(r'(?P<runs>\d+) (?P<capacity>\d+) (?P<groups>\d+)')

def GetNumberOfEnteringGroups(groups, capacity):
    total = 0
    num_of_groups = 0
    for i in groups:
	total += i

	if total <= capacity:
	    num_of_groups += 1
	else:
	    break

    return num_of_groups


def RunRollerCoaster(runs, capacity, groups, num_of_groups):
    earnings = 0

    for run in range(runs):
	num_of_entering_groups = GetNumberOfEnteringGroups(groups, capacity)

	# Deadlock condition
	if num_of_entering_groups == 0:
	    break

	earnings += reduce(lambda x, y: x+y, groups[:num_of_entering_groups])
	groups = groups[num_of_entering_groups:] + groups[:num_of_entering_groups]

    return earnings


if __name__ == '__main__':
    # Command line parsing
    parser = OptionParser()
    (opts, args) = parser.parse_args()

    if len(args) != 1:
	print('ERROR: Supply filename')
	sys.exit(1)

    with open(args[0], 'r') as file_handle:
	cases = int(file_handle.readline())

	for case in range(cases):
	    match = INFO_REGEX.search(file_handle.readline())
	    runs = int(match.group('runs'))
	    capacity = int(match.group('capacity'))
	    num_of_groups = int(match.group('groups'))

	    groups = [int(x) for x in file_handle.readline().strip().split(' ')]
	    if len(groups) != num_of_groups:
		print('ERROR: Number of groups mismatch', groups, len(groups), num_of_groups)
		sys.exit(1)

	    earnings = RunRollerCoaster(runs, capacity, groups, num_of_groups)
	    print('Case #{0:d}: {1}'.format(case+1, earnings))
