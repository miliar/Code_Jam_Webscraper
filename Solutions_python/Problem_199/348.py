FILE = 'A-large.in'

table = str.maketrans('+-','-+')

def solve(line):
    s, k = line.split()
    flips = 0
    s=s.strip('+')
    k=int(k)
    while True:
        if not s: return flips
        if len(s)<k: return float('inf')
        flips+=1
        s=(s[:k].translate(table)+s[k:]).strip('+')

def format_output(case, answer):
    return 'Case #{0}: {1}'.format(case, 'IMPOSSIBLE' if answer==float('inf') else answer)

with open(FILE,'r') as infile:
    with open('output_'+FILE,'w') as outfile:
        infile.readline()
        case_number = 1
        for line in infile:
            outfile.write(format_output(case_number,solve(line.rstrip()))+'\n')
            case_number+=1
        
