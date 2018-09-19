import os

if __name__ == "__main__": 
    f = open('B-large.in', 'r')
    fo = open('B-large.out', 'w')
    T = int(f.readline())
    
    for i in range(0, T):
        print 'case #' + str(i + 1)
        case = f.readline().split()
        combos = case[1:int(case[0]) + 1]
        l = len(combos) + 1
        oposites = case[l + 1:l + int(case[l]) + 1]
        l += len(oposites) + 1
        elist = case[l + 1]
        
        stack = []
        for e in elist:
            if len(stack) == 0:
                stack.append(e)
                continue
            pe = stack[-1]
            b = False
            for com in combos:
                if ''.join([e, pe]) == com[0:2] or ''.join([pe, e]) == com[0:2]:
                    stack.pop()
                    stack.append(com[2])
                    b = True
            if not b:
                for op in oposites:
                    if (op[0] in stack or op[1] in stack) and e in op and e not in stack:
                        stack = []
                        b = True
            if not b:
                stack.append(e)
        
        fo.write('Case #' + str(i + 1) + ': ' + '[' + ', '.join(stack) + ']\n')
                    
    
    f.close()
    fo.close()
