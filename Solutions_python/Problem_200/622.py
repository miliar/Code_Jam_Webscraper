import sys
import itertools

input_file = sys.argv[1]
with open(input_file) as f:
    lines = [line.strip() for line in f]
Ns = [[int(c) for c in line] for line in lines[1:]]

def is_tidy(n):
    return all(c <= d for c,d in zip(n[:-1],n[1:]))

def last_tidy(n):
    result = []
    for i,(c,d) in enumerate(zip(n[:-1],n[1:])):
        if c <= d:
            result.append(c)
        else:
            result.append(c-1)
            result.extend([9]*(len(n)-i-1))
            break
    else:
        result.append(n[-1])
    if is_tidy(result):
        return int(''.join(map(str,result)))
    else:
        return last_tidy(result)

ys = map(last_tidy,Ns)
output_file = input_file.replace('input','output')
with open(output_file,'w') as f:
    for i,y in enumerate(ys):
        f.write(f'Case #{i+1}: {y}\n')
