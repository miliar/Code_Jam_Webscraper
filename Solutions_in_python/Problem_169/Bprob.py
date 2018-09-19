# Import the file
in_file = 'B-small-attempt2.in'
Type = 'small' if in_file.count('small') > 0 else 'large' if in_file.count('large') > 0 else 'test'
out_file = 'B-{0}.out'.format(Type)

with open(in_file,'r') as f:
    data = f.readlines()

data2 = data.copy()
# Format the data
Tt = int(data[0])
del data[0]
    
OUT = []
for k in range(Tt):
    # Enter code here
    N,V,X = data[0].split(' ')
    N = int(N)
    V = float(V)
    X = float(X)
    R = []
    C = []
    for i in range(N):
        temp = list(map(float,data[1+i].split(' ')))
        R.append(temp[0])
        C.append(temp[1])
    del data[:N+1]
    if N == 1:
        if C[0] == X:
            OUT.append(V/R[0])
            continue
        else:
            OUT.append('IMPOSSIBLE')
            continue
    if N == 2:
        if max(C) < X or min(C) > X:
            OUT.append('IMPOSSIBLE')
            continue
        if C[0] == C[1]:
            OUT.append(V/sum(R))
            continue
        V2 = V*(X-C[0])/(C[1]-C[0])
        V1 = V - V2
        OUT.append(max(V2/R[1],V1/R[0]))
    pass
        

with open(out_file,'w') as f:
    for i in range(Tt):
        f.write('Case #{0}: {1}\n'.format(i+1,OUT[i]))
