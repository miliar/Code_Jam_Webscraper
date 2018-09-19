import argparse
from ioutil import ProblemManager

class Settings:
    parse_int = True

def main(handler_func):
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--infile", help="The file to read the problem from", required=True)
    parser.add_argument("-l", "--lines", help="Lines Per Problem (the number of lines in each problem in the input)",
                        type=int, required=True)
    parser.add_argument("-o", "--outfile", help="The file to output the result to", required=False)
    args = parser.parse_args()

    problemManager = ProblemManager(handler_func, args.infile, args.outfile, args.lines)
    problemManager.parse_int = Settings.parse_int
    problemManager.run()
