def is_tidy(number):
    for i in range(len(number) - 1):
        if int(number[i]) > int(number[i+1]):
            return False
    return True

def remove_leading_zeroes(line):
    while len(line) > 1 and line[0] == '0':
        line = line[1:]
    return line

def step_down(number):
    for i in range(len(number) - 1):
        if int(number[i]) > int(number[i+1]):
            number = number[:i] + str(int(number[i]) - 1) + '9' * (len(number) - (i + 1))
            break

    return remove_leading_zeroes(number)

def solve_case(line):
    while not is_tidy(line):
        line = step_down(line)

    return remove_leading_zeroes(line)

def remove_trailing_newlines(text):
    while text[-1] == '\n':
        text = text[:-1]
    return text

FILENAME = 'B-large'
lines = []
with open(FILENAME + '.in') as f:
    text = f.read()
    text = remove_trailing_newlines(text)
    lines = text.split('\n')
    f.close()

lines = lines[1:]
solutions = []

for i in range(len(lines)):
    line = lines[i]
    solution = solve_case(line)
    outline = 'Case #' + str(i + 1) + ': ' + str(solution)
    solutions.append(outline)

with open(FILENAME + '.out', 'w') as f:
    for line in solutions:
        f.write(line + '\n')
    f.close()
