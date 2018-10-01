def algo(replacements, deleters, s):
    stack = []
    flg, dp = False, False
    
    for i in xrange(0, len(s)):
        flg = False
        dp = False

        if len(stack) == 0:
            stack.append(s[i])
            continue

        last = stack[len(stack)-1]
        for r in replacements:
            if last + s[i] == r[:2] or s[i] + last == r[:2]:

                stack.pop()
                stack.append(r[2])
                i += 1

                flg = True
                dp = True
                break
                
        if not flg:
            for d in deleters:
                for k in xrange(0,len(stack)):
                    if stack[k] + s[i] == d or s[i] + stack[k] == d:
                        del stack[:]
                        dp = True
                        break
        if not dp:
            stack.append(s[i])

    return stack


f = open("b.in", "r")
content = f.readlines()

T =  int(content[0])

for i in xrange(1, T+1):
    c = content[i].rstrip("\n").split(" ")

    repl = []
    C = int(c[0])
    for k in xrange(0,C):
        repl.append(c[1+k])

    dels = []
    D = int(c[C+1])
    for j in xrange(2+C, 2+C+D):
        dels.append(c[j])

    s = c[len(c)-1]


    print ("Case #{0}: {1}".format(i, algo(repl, dels, s))).replace("'", "")
