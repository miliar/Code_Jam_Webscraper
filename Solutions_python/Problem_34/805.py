
def belongsTo(rule, k):
    i = 0
    for c in k:
        if c not in rule[i]:
            return False
        i += 1
    return True

def extract_rule(line):        
    seq = []
    while len(line) > 0:
        if(line[0] == '('):
            subseq = []
            line = line[1:]
            while line[0] != ')':
                subseq.append(line[0])
                line = line[1:]
            line = line[1:]
            seq.append(subseq)
        else:
            seq.append([line[0]])
            line = line[1:]
    return seq

params = raw_input().split()
L = int(params[0])
D = int(params[1])
N = int(params[2])

p = []
for i in range(D):
    p.append(raw_input())
    
for n in range(N):
        line = raw_input()
        rule = extract_rule(line)

        i = 0
        for k in p:
            if belongsTo(rule, k):
                i += 1
        print "Case #" + str(n+1) + ": ", i 

            
