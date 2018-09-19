from optparse import OptionParser
from functions import *

parser = OptionParser()

parser.add_option("-p", "--puzzle", dest="puzzle", help="Select which puzzle solver to run", metavar="PUZZLE")

parser.add_option("-i", "--input", dest="input_filename", help="Select which input file to use", metavar="INPUT_FILENAME")

parser.add_option("-o", "--output", dest="output_filename", help="Select which output file to use", metavar="OUTPUT_FILENAME")

parser.add_option("-t", "--test", dest="test", action="store_true", help="Run test script", default=False)

(options, args) = parser.parse_args()

if options.puzzle is None:
	options.puzzle = 'qa'

if options.input_filename is None:
	options.input_filename = 'input'

if options.output_filename is None:
	options.output_filename = 'output'

solver = __import__(options.puzzle)

if options.test:
	solver.test()
else:
	set_puzzle(options.puzzle)
	set_output(open_output(options.output_filename))
	puzzle_input = open_input(options.input_filename) 

	solver.solve(puzzle_input)