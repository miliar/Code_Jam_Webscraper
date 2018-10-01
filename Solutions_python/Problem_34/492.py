import re

def gen_word(s):
    words = []

    l = []
    st = False
    index = 0
    for i in range(len(s)):
        if s[i] == '(':
            st = True
        elif s[i] == ')':
            st = False
        else:
            if s[i] in Fil[index]:
                l.append(s[i])

        if not st:
            index += 1
            if len(words) == 0:
                words = l
            else:
                new = []
                for w in words:
                    for ll in l:
                        for p in Pattern:
                            if p[:index] == w+ll:
                                new.append(w+ll)
                del words
                words = new
            del l
            l = []
    return words


state = 0
Case = 0
#for line in open('A-large.in', 'r'):
#for line in open('A-test', 'r'):
for line in open('A-small-attempt1.in', 'r'):
    while True:
        if state == 0:
            r = re.compile("^([0-9]+) ([0-9]+) ([0-9]+)$")
            m = r.search(line[:-1])
            L = int(m.group(1))
            D = int(m.group(2))
            N = int(m.group(3))

            state = 1
            Pattern = set([])
            break
        elif state == 1:
            if len(Pattern) == D:
                Words = []
                state = 2
                Fil = [set([]) for i in range(L)]
                for p in Pattern:
                    for i in range(L):
                        Fil[i].add(p[i])
                continue
            Pattern.add(line[:-1])
            break
        elif state == 2:
            if len(Words) == N:
                state = 3
                continue
            Words.append(line[:-1])
            w = set(gen_word(Words[-1])) & Pattern
            Case += 1
            print "Case #"+str(Case)+": "+str(len(w))
            break
        elif state == 3:
            print "end"
            break


