#!/usr/bin/python

import os
import sys

USAGE = "Usage: python %s INPUT_FILE" % (sys.argv[0])

def main(argv=None):
	if argv is None:
		argv = sys.argv
	
	if len(argv) != 2:
		print USAGE
		return 1
	
	input_filename = argv[1]
	
	params = InputParameters(input_filename)
	
	i = 1
	for test_case in params.test_case_list:
		print "Case #%d: %s" % (i, test_case.get_light_bulb_state())
		i += 1

class TestCase:
	def __init__(self):
		self.N = None
		self.K = None
	
	def get_light_bulb_state(self):
		if self.N is None or self.K is None:
			return "INVALID_ARGS"
		
		if self.K < self.N:
			return "OFF"
		
		state_chain = 0
		power_chain = 1
		
		for snap in range(0, self.K):
			state_chain ^= power_chain
			power_chain = 1
			for i in range(0, 32):
				if (1 << i) & state_chain & power_chain:
					power_chain = (power_chain << 1) | 1
				else:
					break
		
		if (1 << (self.N-1)) & state_chain & power_chain:
			return "ON"
		else:
			return "OFF"
		
		return "IDK"

class InputParameters:
	def __init__(self, input_filename=None):
		self.T = None
		self.test_case_list = []
		
		if input_filename is not None:
			self.parse_input_file(input_filename)
	
	def parse_input_file(self, input_filename):
		if not os.path.exists(input_filename):
			return -1
		elif not os.path.isfile(input_filename):
			return -2
		
		input_file = open(input_filename, "r")
		lines = [l.rstrip() for l in input_file.readlines()]
		
		if len(lines) < 1:
			return -3
		
		self.T = int(lines[0])
		
		for i in range(1, self.T+1):
			test_case = TestCase()
			test_case.N, test_case.K = tuple([int(l) for l in lines[i].split()])
			self.test_case_list.append(test_case)
		
		input_file.close()
		return 0

if __name__ == "__main__":
	sys.exit(main())

