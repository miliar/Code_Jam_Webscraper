
def read_ints():
    return map(int, raw_input().split(" "))


def do_comp(stack, comp_m):
    def found():
        if len(stack) >= 2 and stack[-2:] in comp_m:
            return comp_m[stack[-2:]]
        return None
    while True:        
        op = found()
        if op == None:
            break;
        stack = stack[0:-2]
        stack += op
    return stack

def do_clear(stack, opp):
    for op in opp:
        a = op[0]
        b = op[1]
        if a in stack and b in stack:
            stack = ""
            break;
    return stack

T, = read_ints()
for cas in range(T):
    line = raw_input().split(" ")

    C = int(line[0])
    comp = line[1:1+C]
    D = int(line[1+C])
    opp = line[2+C:2+C+D]
    act = line[-1] 
    #print comp, opp, act

    comp_m = {}
    for c in comp:
        a = c[0]
        b = c[1]
        c = c[2]
        comp_m[a + b] = c
        comp_m[b + a] = c

    stack = ''
    for ch in act:
        stack += ch
        l = len(stack)
       
        #print "before: " + stack
        stack = do_comp(stack, comp_m)
        #print "comp: " + stack

        stack = do_clear(stack, opp)
        #print "oppose " + stack
        #print
    
    print "Case #%d: [%s]" % (cas+1, ", ".join(stack))




