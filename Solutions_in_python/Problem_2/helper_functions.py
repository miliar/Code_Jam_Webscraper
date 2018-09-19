#!/usr/bin/python
""""
helper_functions.py

Things that are used in all problems. 
I will upload this at the end of each round if it changes.

"""
import sys
import os.path
import StringIO


case_no = 0
def init():
    global case_no
    case_no = 0

def getnum(input):
    return int(getline(input))

def getwords(input):
    return getline(input).split()

def getline(input):
    return input.readline().strip()

readline = getline # alias

def answer(result, outfile=None):
    """outputs Case #n: str(string)\\n"""
    global case_no
    case_no += 1
    if isinstance(result, str):
        string = result
    elif isinstance(result, (list, tuple)):
        string = ' '.join(str(i) for i in result)
    else:
        string = str(result)
    out = 'Case #' + str(case_no) + ': ' + string + '\n'
    if outfile:
        outfile.write(out)
    else:
        return out

def equal(answer_1, answer_2):
    for words in zip(answer_1.split(), answer_2.split()):
        if words[0]!=words[1]:
            print words[0],words[1]
            return False
    if len(answer_1.split()) != len(answer_2.split()):
        return False
    else:
        return True

def do_real(solving_function):
    init()
    input_filename = sys.argv[1]
    output_filename = sys.argv[2]
    input = open(input_filename, 'r')
    output = open(output_filename, 'w')
    solving_function(input, output)
    output.close()
    print "upload", os.path.abspath(output_filename)
    
def do_test(function, test_input, test_output):
    init()
    input = StringIO.StringIO(test_input.strip())
    output = StringIO.StringIO()
    function(input, output)
    answers = output.getvalue()
    assert equal(answers, test_output), "your answers:\n" + answers + "the right anwers:\n" + test_output
    print "Test Passed.\n"
