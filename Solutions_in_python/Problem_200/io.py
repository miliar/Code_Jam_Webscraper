import my_sol

inp_name = 'B-small-attempt0.in'
out_name = 'small.out'

_input = open(inp_name, 'r')  # small.in needs to be in the same dir as this file
output = open(out_name, 'w') # small.out will be created in this dir if it doesn't already exist

T = int( _input.readline() )

for x in range(1, T+1):
    N = int( _input.readline() )
    y = my_sol.general(N)
    out = 'Case #{}: {}\n'.format(x, y)
    output.write( out )

_input.close()
output.close()