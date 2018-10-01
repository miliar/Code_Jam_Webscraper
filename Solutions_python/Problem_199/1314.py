#--- READ INPUT ---#
#inp = open('A-small-attempt0.in', 'r')
inp = open('A-large.in', 'r')
#inp = open('test.in', 'r')
o = open('output-large.txt', 'w')

test_cases = int(inp.readline())
for i in range(test_cases):
    l = inp.readline().split(' ')
    k = int(l[1])
    l = [c for c in l[0]]

    #--- SOLUTION ---#
    moves = 0
    for j in range(len(l) -k +1):
        if l[j] == '-':
            l[j:j+k] = ['+' if c == '-' else '-' for c in l[j:j+k]]
            moves += 1
    res = moves
    for e in l:
        if e == '-':
            res = 'IMPOSSIBLE'

    #--- WRITE OUTPUT ---#
    s = 'Case #' + str(i+1) + ': ' + str(res)
    o.write(s + '\n')
inp.close()
o.close()
