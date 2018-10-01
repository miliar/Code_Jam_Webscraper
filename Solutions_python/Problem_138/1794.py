def playwar(n,k,score):
    if len(n) == 0:
        return score
    nval = n.pop(0)
    burn = 0
    for x in k:
        if x > nval:
            burn = x
            break
    if burn == 0:
        score+=1
        k.pop(0)
    else:
        k.remove(burn)
    return playwar(n,k,score)

def playdeceit(n,k,score):
    l = len(n)
    if l == 0:
        return score
    nval = n.pop(0)
    if nval > k[0]:
        k.pop(0)
        score+=1
    else:
        kval = k.pop(l-1)
        if nval > kval:
            score+=1
    return playdeceit(n,k,score)

def solve(lines):
    naomi = sorted([float(x) for x in lines[1].split(" ")])
    ken = sorted([float(x) for x in lines[2].split(" ")])
    return "%s %s " % (playdeceit(naomi[:],ken[:],0),playwar(naomi[::1],ken[:],0))


input_text = [line.strip() for line in open('q3s.txt')]
CASE_COUNT = int(input_text[0])
NUM_EACH_CASE = 3
for CASE_NUM in range(1,CASE_COUNT+1):
    start = (CASE_NUM-1)*NUM_EACH_CASE+1
    end = start + NUM_EACH_CASE
    arr = [x for x in input_text[start:end]]
    print "Case #%d: %s" % (CASE_NUM,solve(arr))
