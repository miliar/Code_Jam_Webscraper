f = open('Google Standing Ovation Large.in','r')
g = open('Google Standing Ovation Large.out','w')

def Google_print(filename,answers):
    for i in range(len(answers)):
        filename.write("Case #%s: %s\n" % (str(i+1),answers[i]))
        print "Case #%s: %s" % (str(i+1),answers[i])
    return

def ringers(s):
    a = []
    for i in range(len(s)):
        k = int(s[i])
        t = [i]*k
        a.extend(t)
    a.reverse()
    answer = 0
    standing = 0
    while a:
        x = a.pop()
        if x <= standing:
            standing += 1
        else:
            answer += x-standing
            standing += (x-standing)+1
    return answer

cases = int(f.readline())
answers = []
for i in range(cases):
    line = f.readline().rstrip().split(' ')
    s = line[-1]
    answers.append(ringers(s))
Google_print(g,answers)
f.close()
g.close()
