"""
Google Code Jam 2009, Round 1, Problem A
"""
import array
import decimal
import itertools
import logging
import math
from optparse import OptionParser
import os
import sys

logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s')
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

# decimal.getcontext().prec = 28

class InvalidParameter(Exception):
    pass


class Answerer(object):
    def __init__(self, params):
        self.params = params

    def solve(self):
        self.initialize()
        self.solve_all_cases()
        self.finalize()

    def initialize(self):
        self.problem_data = {}
        self.open_input()
        self.open_output()

    def finalize(self):
        self.close_input()
        self.close_output()
        del self.problem_data

    def open_input(self):
        input_abspath = self.params["input_abspath"]
        if input_abspath:
            input = open(input_abspath, "r")
        else:
            input = sys.stdin
        self.input = input

    def close_input(self):
        assert self.input.read() == "", "unexpected input data"
        self.input.close()

    def open_output(self):
        output_abspath = self.params["output_abspath"]
        if output_abspath:
            output = open(output_abspath, "w")
        else:
            output = sys.stdout
        self.output = output

    def close_output(self):
        self.output.flush()
        self.output.close()

    def solve_all_cases(self):
        self.make_problem_data()
        for case_id in range(1, self.problem_data["n_case"] + 1):
            logger.info("solving Case #%d ...", case_id)
            self.start_case(case_id)
            self.solve_case()
            self.end_case()

    def make_problem_data(self):
        T = int(self.input.readline().rstrip("\n"))
        logger.info("T=%d", T)

        self.problem_data["n_case"] = T

    def start_case(self, case_id):
        self.case_data = {'case_id': case_id}

        N = int(self.input.readline().rstrip("\n"))
        self.case_data["N"] = N

        initial_conditions = []
        for i in range(N):
            x, y, z, vx, vy, vz = map(decimal.Decimal, self.input.readline().rstrip("\n").split(" "))
            initial_conditions.append(dict(
                    x=x,
                    y=y,
                    z=z,
                    vx=vx,
                    vy=vy,
                    vz=vz
                ))
        #logger.info(initial_conditions)
        self.case_data["initial_conditions"] = initial_conditions

    def end_case(self):
        del self.case_data

    def solve_case(self):
        initial_conditions = self.case_data["initial_conditions"]

        VX = VY = VZ = X = Y = Z = decimal.Decimal("0.0")

        for d in initial_conditions:
            VX += d['vx']
            VY += d['vy']
            VZ += d['vz']

            X += d['x'] 
            Y += d['y'] 
            Z += d['z'] 

        logger.info("X=%f,Y=%f,Z=%f,VX=%f,VY=%f,VZ=%f",X, Y, Z, VX, VY, VZ)    

        t2 = VX**2 + VY**2 + VZ**2
        t1 = decimal.Decimal("2.0") * (VX * X + VY * Y + VZ * Z)
        t0 = X**2 + Y**2 + Z**2

        if t2 == decimal.Decimal("0.0"):
            t_min = decimal.Decimal("0.0")
        else:
            t_min = - t1 / t2 * decimal.Decimal("0.5")
            if t_min < decimal.Decimal("0.0"):
                t_min = decimal.Decimal("0.0")

        d_min = (X + t_min * VX) ** 2 + (Y + t_min * VY) **2 + (Z + t_min * VZ) ** 2
        d_min = math.sqrt(d_min) / self.case_data["N"]

        self.output.write(
            "Case #%d: %.8f %.8f\n" % (self.case_data["case_id"], d_min, t_min)
            )


def add_options(opt_parser):
    opt_parser.add_option("-d", "--dir",
                          dest="dir", 
                          help="base directory for <input> and <output>",
                          metavar="DIR",
                          default=None)
    opt_parser.add_option("-i", "--input",
                          dest="input", 
                          help="input file, relative path to <dir>",
                          metavar="FILE",
                          default=None)
    opt_parser.add_option("-o", "--output",
                          dest="output", 
                          help="output file, relative path to <dir>",
                          metavar="FILE",
                          default=None)
    opt_parser.add_option("-v", "--verbose",
                          dest="verbose", 
                          help="enable logging",
                          action="store_true",
                          default=False)
    return opt_parser

def get_params(options):
    params = {}
    error = []

    param_list = ["dir", "input", "output", "verbose"]

    for key in param_list:
        params[key] = getattr(options, key)

    if not params["dir"]:
        params["dir"] = os.getcwd()

    if not os.path.exists(params["dir"]):
        error.append("<%s> not found." % dir)
    else:    
        for f in ["input", "output"]:
            if not params[f]:
                params[f + "_abspath"] = None
                continue

            f_abspath = os.path.join(params["dir"], params[f])
            params[f + "_abspath"] = f_abspath
            
            if f == "output" and os.path.exists(f_abspath):
                error.append("%s already exists." % f_abspath)

    if params["verbose"]:
        logging.getLogger().setLevel(logging.DEBUG)
    else:    
        logging.getLogger().setLevel(logging.ERROR)

    if error:
        raise InvalidParameter, "\n".join(error)
    else:
        return params

def main(argv):
    """Usage: %(prog)s [options]
    """

    opt_parser = OptionParser(usage=main.__doc__ % dict(prog=__file__) + \
                                  "\nDescription: " + __doc__.strip(),
                              version="1.0")
    opt_parser = add_options(opt_parser)
    (options, args) = opt_parser.parse_args(args=argv)

    try:
        params = get_params(options)
    except InvalidParameter, e:
        logging.error(e)
        opt_parser.print_help()
        raise SystemExit
    
    logger.info("start")
    logger.info(params)
    answerer = Answerer(params)
    answerer.solve()
    logger.info("end")

if __name__ == '__main__':
    main(sys.argv)
