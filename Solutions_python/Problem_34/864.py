import sys, re
line = sys.stdin.readline().strip()
r = line.split(" ")
lang_lenght = int(r[0])
lang_word_count = int(r[1])
lang_test_cases = int(r[2])
words = []
patterns = []

for i  in range(0, lang_word_count):
    words.append(sys.stdin.readline().strip())

for i in range(0, lang_test_cases):
    patterns.append(sys.stdin.readline().strip())


def word_matches_pattern(w, p):
    pattern = "^"
    for l in w:
        pattern = pattern + ("(%s|\(.*%s.*\))" % (l, l))
    pattern = pattern + "$"
    exp = re.compile(pattern)
    return exp.match(p)

def count_matches(p):
    c = 0
    for w in words:
        if word_matches_pattern(w, p):
            c = c+1
    return c


counter = 1
for p in patterns:
    print "Case #%d: %d" % (counter, count_matches(p)) 
    counter = counter + 1

        
        
