import random
import sys

debug = False

class Rule:
    def __init__(self, left, right):
        self.left = left
        self.right = right
    
    def applies(self, line):
        return self.left in line
    
    def apply(self, line):
        return line.replace(self.left, self.right, 1)

    def __str__(self):
        return "{}::={}".format(self.left, self.right)

class InputRule:
    def __init__(self, left):
        self.left = left
    
    def applies(self, line):
        return self.left in line

    def apply(self, line):
        return line.replace(self.left, sys.stdin.readline().strip(), 1)

class NewLineRule:
    def __init__(self, left):
        self.left = left
    
    def applies(self, line):
        return self.left in line
    
    def apply(self, line):
        print
        return line.replace(self.left, "", 1)

class OutputRule:
    def __init__(self, left, right):
        self.left = left
        self.right = right
    
    def applies(self, line):
        return self.left in line
    
    def apply(self, line):
        sys.stdout.write(self.right)
        return line.replace(self.left, "", 1)

class Program:
    def __init__(self, rules):
        self.rules = rules
    
    def apply(self, line):
        while True:
            relevants = [rule for rule in self.rules if rule.applies(line)]
            if not any(True for rule in relevants):
                break
            choice = random.choice(relevants)
            line = choice.apply(line)
            if debug:
                print >>sys.stderr, "Rule: {}".format(choice)
            if debug:
                print >>sys.stderr, "Line: {}".format(line)
                print >>sys.stderr, ""

def runThue(filename):
    rules = []
    with open(filename) as file:
        for line in file:
            line = line.rstrip("\r\n")
            if line == "::=":
                break
            (left,right) = line.split("::=",1)
            if right == "~":
                rules.append(NewLineRule(left))
            elif right.startswith("~"):
                rules.append(OutputRule(left, right[1:]))
            elif right == ":::":
                rules.append(InputRule(left))
            else:
                rules.append(Rule(left, right))
        program = Program(rules)
        lines = []
        for line in file:
            lines.append(line)
        text = "".join(lines)
        program.apply(text)

if __name__ == "__main__":
    runThue(sys.argv[1])
