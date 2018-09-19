def fixed_sepa(fulltext, problemtexts, linesperproblem):
    numprobs = int(fulltext[0].rstrip())
    index = 1
    for x in range(numprobs):
        problemtexts.append(fulltext[index:index+linesperproblem])
        index += linesperproblem
        pass
    pass

class ProbSepaFixed:
    def separate(self, fulltext, problemtexts):
        fixed_sepa(fulltext, problemtexts, self.linesperproblem)
        pass
    pass

def out_form(outputobject, outputtext, casenumber, real_form):
    string = 'Case #' + str(casenumber) + ': '
    string += real_form(outputobject)
    string += '\n'
    outputtext.append(string)
    pass

def real_form_answer(outputobject):
    return str(outputobject.answer)

class OutPutForm:
    def formato(self, outputobject, outputtext):
        out_form(outputobject, outputtext, self.casenumber, self.real_form)
        self.casenumber += 1
        pass
    pass

def read3nums(problemtext, problemobject):
    strings = problemtext[0].rstrip().split()
    problemobject.low = int(strings[0])
    problemobject.high = int(strings[1])
    problemobject.factor = int(strings[2])
    pass

class ProbCompTrip:
    def compose(self, problemtext, problemobject):
        read3nums(problemtext, problemobject)
        pass
    pass

def algo(po, oo):
    import math
    answer = 0
    while(po.high/po.low > po.factor):
        po.high = math.ceil(math.sqrt(po.low*po.high))
        answer += 1
    oo.answer = answer
    pass

class AlgoSum:
    def run(self, problemobject, outputobject):
        algo(problemobject, outputobject)
        pass
    pass

def runprog(infile, outfile):
    import framework
    proc = framework.Processor()
    
    proc.problem_separator = ProbSepaFixed()
    proc.problem_separator.linesperproblem = 1
    
    proc.problem_composer = ProbCompTrip()

    proc.algorithm = AlgoSum()
    
    proc.output_formatter = OutPutForm()
    proc.output_formatter.casenumber = 1
    proc.output_formatter.real_form = real_form_answer

    framework.solution(infile, outfile, proc)
    pass
