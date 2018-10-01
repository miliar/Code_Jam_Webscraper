f = open ("C-small-attempt0.in", "r")
l = f.readlines ()
n = int(l[0])
l.pop (0)

for b in range(n):
    solutions = []
    couple = tuple(l[b].strip ().split (" "))
    if len(couple[0]) == len(couple[1]):
        check = False
    else:
        check = True
    for number in range(int(couple[0]), int(couple[1])+1):
        s = str(number)
        length = len(s)
        if length != 1:
            for sec_num in range(number, int(couple[1])+1):
                for i in range (1, length):
                    if int(s[i:] + s[:i]) == sec_num and int(s) != sec_num:
                        ss = int(s)
                        if ss > sec_num:
                            c = (sec_num, ss)
                        else:
                            c = (ss, sec_num)
                        if c not in solutions:
                            solutions.append (c)
    print "Case #%s: " % (b+1) + str(len(solutions))
