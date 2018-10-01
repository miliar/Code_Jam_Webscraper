input_lines = []

with open('/Users/agrandhi/desktop/input.txt', 'r') as f:
    lines = f.readlines()

o = open('/Users/agrandhi/desktop/output.txt', 'w')

n = len(lines)
j = 1

for i in range(1, n, 10):
    c1 = set(lines[i+1 : i+5][int(lines[i].strip())-1].strip().split())
    c2 = set(lines[i+6 : i+10][int(lines[i+5].strip())-1].strip().split())

    matches = len(c1 & c2)
    if matches == 0:
        ans = 'Volunteer cheated!'
    elif matches > 1:
        ans = 'Bad magician!'
    else:
        ans = c1 & c2

    o.write('Case #%s: %s\n' % (j, ''.join(ans)))
    j = j + 1

o.close()
