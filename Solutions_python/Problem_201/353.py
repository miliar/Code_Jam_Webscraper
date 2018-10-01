FILE = 'C-large.in'

def occupy(n):
    a,b = divmod(n-1,2)
    return (a+b,a)

def solve(line):
    n, k = map(int,line.split())
    stalls = {n: 1}
    while True:
        widest = max(stalls)
        number = stalls.pop(widest)
        if k<=number: return occupy(widest)
        k-=number
        for width in occupy(widest): stalls[width]=number+stalls.get(width,0)
    

def format_output(case, answer):
    return 'Case #{0}: {1} {2}'.format(case,*answer)

with open(FILE,'r') as infile:
    with open('output_'+FILE,'w') as outfile:
        infile.readline()
        case_number = 1
        for line in infile:
            outfile.write(format_output(case_number,solve(line.rstrip()))+'\n')
            case_number+=1
        
