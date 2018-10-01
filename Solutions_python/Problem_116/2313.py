# Codejam 2013
# Problem A. Tic-Tac-Toe-Tomek

#inputFilename = 'problem.input'
inputFilename = 'A-large.in'

###################
input = open(inputFilename, 'r').readlines()
casesCount = int(input[0].strip())
cases = {}

# Translate cases into a separate sets: cases
i = pos = 1
while i <= casesCount:
    cases[i] = [[input[pos][0],input[pos][1],input[pos][2],input[pos][3].strip()], 
                [input[pos+1][0],input[pos+1][1],input[pos+1][2],input[pos+1][3].strip()], 
                [input[pos+2][0],input[pos+2][1],input[pos+2][2],input[pos+2][3].strip()], 
                [input[pos+3][0],input[pos+3][1],input[pos+3][2],input[pos+3][3].strip()]]
    i += 1
    pos = pos + 5
    
class CaseResult(Exception):
    def __init__(self, value):
        self.value = value
    
    def __str__(self):
        return repr(self.value)

class Case:
    result = ['X won', 'O won', 'Draw', 'Game has not completed']
    resultMap = {'X': 0, 'O': 1, 'D': 2}
    
    def __init__(self, case):
        self.size = len(case[0])
        self.case = case
        
    def evaluate(self):
        possiblyIncomplete = False
    
        try:
            # 1. Horizontal check
            x = y = 0
            for y in range(self.size):
                square = self.case[y][x]
                
                # Check if the row is complete
                if square == '.' or self.case[y][x+1] == '.' or self.case[y][x+2] == '.' or self.case[y][x+3] == '.':
                    possiblyIncomplete = True
                    continue
                    
                # Determine what to check for
                if square != 'T':
                    checkFor = [square, 'T']
                if square == 'T':
                    if self.case[y][x+1] == '.':
                        possiblyIncomplete = True
                        continue
                    else:
                        checkFor = [self.case[y][x+1], 'T']
                
                
                if square in checkFor and self.case[y][x+1] in checkFor and self.case[y][x+2] in checkFor and self.case[y][x+3] in checkFor:
                    raise CaseResult(self.resultMap[checkFor[0]])

            # 2. Vertical check
            x = y = 0
            for x in range(self.size):
                square = self.case[y][x]
                
                # Check if the column is complete
                if square == '.' or self.case[y+1][x] == '.' or self.case[y+2][x] == '.' or self.case[y+3][x] == '.':
                    possiblyIncomplete = True
                    continue
                    
                # Determine what to check for
                if square != 'T':
                    checkFor = [square, 'T']
                if square == 'T':
                    if self.case[y+1][x] == '.':
                        possiblyIncomplete = True
                        continue
                    else:
                        checkFor = [self.case[y+1][x], 'T']
                
                
                if square in checkFor and self.case[y+1][x] in checkFor and self.case[y+2][x] in checkFor and self.case[y+3][x] in checkFor:
                    raise CaseResult(self.resultMap[checkFor[0]])
                
            # 3. Left to right diagonal check
            x = y = 0
            try:
                square = self.case[y][x]

                # Check if the diagonal is complete
                if square == '.' or self.case[y+1][x+1] == '.' or self.case[y+2][x+2] == '.' or self.case[y+3][x+3] == '.':
                    possiblyIncomplete = True
                    raise Exception()
                    
                # Determine what to check for
                if square != 'T':
                    checkFor = [square, 'T']
                if square == 'T':
                    if self.case[y+1][x+1] == '.':
                        possiblyIncomplete = True
                        raise Exception()
                    else:
                        checkFor = [self.case[y+1][x+1], 'T']
                
                
                if square in checkFor and self.case[y+1][x+1] in checkFor and self.case[y+2][x+2] in checkFor and self.case[y+3][x+3] in checkFor:
                    raise CaseResult(self.resultMap[checkFor[0]])
            except Exception as e:
                # Do nothing if its not a CaseResult
                if isinstance(e, CaseResult):
                    raise
                else:
                    pass
            
            # 3. Right to left diagonal check
            x = 3
            y = 0
            try:
                square = self.case[y][x]

                # Check if the diagonal is complete
                if square == '.' or self.case[y+1][x-1] == '.' or self.case[y+2][x-2] == '.' or self.case[y+3][x-3] == '.':
                    possiblyIncomplete = True
                    raise Exception()
                    
                # Determine what to check for
                if square != 'T':
                    checkFor = [square, 'T']
                if square == 'T':
                    if self.case[y+1][x-1] == '.':
                        possiblyIncomplete = True
                        raise Exception()
                    else:
                        checkFor = [self.case[y+1][x-1], 'T']
                
                
                if square in checkFor and self.case[y+1][x-1] in checkFor and self.case[y+2][x-2] in checkFor and self.case[y+3][x-3] in checkFor:
                    raise CaseResult(self.resultMap[checkFor[0]])
            except Exception as e:
                # Do nothing if its not a CaseResult
                if isinstance(e, CaseResult):
                    raise
                else:
                    pass

            if possiblyIncomplete:
                raise CaseResult(3)
            else:
                raise CaseResult(2)
        except CaseResult as e:
            return self.result[int(e.value)]
        
        
# Iterate through cases and evaluate to prepare output
for i in cases:
    case = Case(cases[i])
    print 'Case #%s: %s' % (i, case.evaluate())

#case = Case(cases[1])
#case.evaluate()