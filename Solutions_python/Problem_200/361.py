FILE = 'B-large.in'

def solve(line):
    n=int(line)
    if n<int('1'*len(line)): return '9'*(len(line)-1)
    for i in range(len(line)-1):
        if line[i+1]=='0' or line[i+1]<line[i]:
            return solve(''.join((line[:i],str(int(line[i])-1),'9'*(len(line)-i-1))))
    return line

def format_output(case, answer):
    return 'Case #{0}: {1}'.format(case,answer)

with open(FILE,'r') as infile:
    with open('output_'+FILE,'w') as outfile:
        infile.readline()
        case_number = 1
        for line in infile:
            outfile.write(format_output(case_number,solve(line.rstrip()))+'\n')
            case_number+=1
        
