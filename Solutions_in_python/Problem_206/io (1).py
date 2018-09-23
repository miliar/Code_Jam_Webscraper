import my_sol

# inp_name = 'test.in'
# out_name = 'test.out'

# inp_name = 'A-small-attempt0.in'
# out_name = 'A-small-attempt0.out'

inp_name = 'A-large.in'
out_name = 'A-large.out'

_input = open(inp_name, 'r')  # small.in needs to be in the same dir as this file
output = open(out_name, 'w') # small.out will be created in this dir if it doesn't already exist

T = int( _input.readline() )

for x in range(1, T+1):
    D, N = map(int, _input.readline().split(' '))
    
    KSpairs = [None]*N
    for i in range(N):
        KSpairs[i] = tuple(map(int, _input.readline().split(' ')))
    
    y = my_sol.max_speed(D, N, KSpairs)
    out = 'Case #{}: {}\n'.format(x, y)
    output.write( out )

_input.close()
output.close()