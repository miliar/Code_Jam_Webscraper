# Import the file
in_file = 'A-small-attempt0.in'
Type = 'small' if in_file.count('small') > 0 else 'large' if in_file.count('large') > 0 else 'test'
out_file = 'A-{0}.out'.format(Type)

with open(in_file,'r') as f:
    data = f.readlines()

data2 = data.copy()
# Format the data
Tt = int(data[0])
del data[0]

OUT = []
for k in range(Tt):
    # Enter code here
    R,C,W = list(map(int,data[k].split(' ')))
    # Assume R is 1
    if R == 1:
        if C%W == 0:
            OUT.append(C//W-1+W)
        else:
            OUT.append(C//W+(W if W > 1 else 0))
    else:
        if C%W == 0:
            OUT.append(R*C//W-1+W)
        else:
            OUT.append(R*C//W+(W if W > 1 else 0))
    pass

with open(out_file,'w') as f:
    for i in range(Tt):
        f.write('Case #{0}: {1}\n'.format(i+1,OUT[i]))
