import Google_Code_Jam.problem_solver as gcj_solver

# Used for testing
reload(gcj_solver)

import logger

import copy
import os


inputs = ["ejp mysljylc kd kxveddknmc re jsicpdrysi",
"rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd",
"de kr kd eoya kw aej tysr re ujdr lkgc jv"]

outputs = ["our language is impossible to understand",
"there are twenty six factorial possibilities",
"so it is okay if you want to just give up"]

alphabet = dict()
for in1,out1 in zip(inputs,outputs):
    for a,b in zip(in1, out1):
        alphabet[a] = b

alphabet['z'] = 'q'
alphabet['q'] = 'z'
        
full_alphabet = 'abcdefghijklmnopqrstuvwxyz'
for letter in full_alphabet:
    if letter not in alphabet.keys():
        print "missing key: ", letter
    if letter not in alphabet.values():
        print "missing value: ", letter

def run_unit_tests():
    """
    Runs all the unit tests
    """

    #solver = Solver()



    for a in alphabet:
        print a, alphabet[a]


        
    print "All tests passed"




class Solver(gcj_solver.ProblemSolver):

    
    def __init__(self):
        base_path = "/home/chris/all_code/Python/Google_Code_Jam/2012/Qualification_Round/Problem_B"
        

        """
        fname = 'B-small-attempt0'
        gcj_solver.ProblemSolver.__init__(
            self,
            os.path.join(base_path, fname + '.in'),
            os.path.join(base_path, fname + '.out'),
            True,
            o_debug_file = os.path.join(base_path, fname + '.debug'))
        """

        fname = 'B-large'
        gcj_solver.ProblemSolver.__init__(
            self,
            os.path.join(base_path, fname + '.in'),
            os.path.join(base_path, fname + '.out'),
            True,
            o_debug_file = os.path.join(base_path, fname + '.debug'))



        """
        gcj_solver.ProblemSolver.__init__(
            self,
            os.path.join(base_path, "B-large-practice.in"),
            os.path.join(base_path, "B-large-practice.out"),
            True,
            o_debug_file = os.path.join(base_path, "B-large-practice.debug"))
        """


        self._force_printing = False
        self._debug = True

        # Problem parameters
        self._N = None
        self._S = None
        self._p = None
        self._pts = None

                       
    def get_case_input(self):
        """
        See base class
        """

        self._reset_input_vars()

        first_line = self._in_file.readline().strip()
        inputs = first_line.split(' ')
        self._N = int(inputs[0])
        self._S = int(inputs[1])
        self._p = int(inputs[2])

        self._pts = []
        for total_score in inputs[3:]:
            self._pts.append(total_score)



    def _reset_input_vars(self):
        # Resets input variables
        pass

    def _cleanup(self):
        pass


    def _init(self):
        pass


    def solve_case(self):
        logger.log("N:{N}, S:{S}, p:{p}, pts:{pts}".format(N=self._N,S=self._S,p=self._p,pts=self._pts), i_force=True, o_log_file=self._debug_file)


        no_surprise = self._p + (2 * max(self._p - 1, 0))
        surprise = self._p + (2 * max(self._p - 2, 0))

        #print "no surprise" , no_surprise
        #print "surprise" , surprise
        num_surprises_counted = 0

        res = 0
        for tot_score in self._pts:
            tot_score = int(tot_score)
            if tot_score >= no_surprise:
                #print "won: no surprise with ", tot_score
                res += 1
            elif (num_surprises_counted < self._S) and (tot_score >= surprise):
                #print "won: surprise with ", tot_score
                res += 1
                num_surprises_counted +=1

                
        return [res]
    




if __name__ == "__main__":

    #run_unit_tests()
    

    solver = Solver()

    print("running tests")
    solver.solve()

