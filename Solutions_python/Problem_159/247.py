# Import the file
with open('A-large.in','r') as f:
    data = f.readlines()

# Format the data
T = int(data[0])
del data[0]

OUT = []
for k in range(T):
    N = int(data[0])
    del data[0]
    States = [int(el) for el in data[0].split(' ')]
    del data[0]
    M1 = sum([max(i-j,0) for i,j in zip(States[:-1],States[1:])])
    # First find the rate
    M2R = max([i-j for i,j in zip(States[:-1],States[1:])])
    # Then go through and check non-negativity
    #print(M2R,[min(el,M2R) for el in States[:-1]])
    M2 = sum([min(el,M2R) for el in States[:-1]])
    OUT.append([M1,M2])

with open('A.out','w') as f:
    for i in range(T):
        f.write('Case #{0}: {1} {2}\n'.format(i+1,OUT[i][0],OUT[i][1]))
