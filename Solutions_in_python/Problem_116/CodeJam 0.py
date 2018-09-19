def initialize(List):
    str1 = raw_input().upper()
    str2 = raw_input().upper()
    str3 = raw_input().upper()
    str4 = raw_input().upper()
    print
    List.append([str1,str2,str3,str4])
    return List

def verify_line(line):
    if line.count('X') == 4 or (line.count('X') == 3 and line.count('T') == 1):
        return 1
    elif line.count('O') == 4 or (line.count('O') == 3 and line.count('T') == 1):
        return 2
    else:
        return 0

def verify_col(column_line, counter):
    string = ''
    for i in range(4):
        string += column_line[i][counter]
    return verify_line(string)

def verify_rows(List):
    for i in range(4):
        result = verify_line(List[i])
        if result != 0:
            return result
    return 0

def verify_columns(List):
    for i in range(4):
        result = verify_col(List, i)
        if result != 0:
            return result
    return 0

def verify_main_diag(List):
    string = ''
    for i in range(4):
        string += List[i][i]
    return verify_line(string)

def verify_sec_diag(List):
    string = ''
    for i in range(4):
        string += List[3-i][i]
    return verify_line(string)

def count_dot(List):
    dots = 0
    for i in range(4):
        dots += List[i].count('.')
    if dots == 0:
        return False
    else:
        return True

def verify(List):
    ansList = [verify_rows(List),verify_columns(List),verify_main_diag(List),verify_sec_diag(List)]
    if ansList.count(0) == 4:
        if count_dot(List) == True:
            return -1
        return 0
    else:
        for i in range(4):
            if ansList[i] != 0:
                return ansList[i]

def parser(number):
    if number == -1:
        return "Game has not completed"
    if number == 0:
        return "Draw"
    if number == 1:
        return "X won"
    if number == 2:
        return "O won"

def parse(List,counter):
    answer = parser(verify(List))
    return "Case #"+str(counter)+": " + answer
    
lines = [line.strip() for line in open("A-large.in")]
while lines.count('') != 0:
    lines.remove('')
    
LIST = []
ANSWER = []

test_cases = int(lines.pop(0))

for test in range(test_cases):
    LIST = lines[:4]
    for i in range(4):
        lines.pop(0)
    ANSWER.append(parse(LIST,test+1))

fo = open("output.txt", "w")

for test in range(test_cases):
    fo.write("%s\n" % ANSWER[test])

fo.close()
    
    
        

