import my_sol

inp_name = 'A-large.in'
out_name = 'A-large.out'

_input = open(inp_name, 'r')  # small.in needs to be in the same dir as this file
output = open(out_name, 'w') # small.out will be created in this dir if it doesn't already exist

T = int( _input.readline() )

sol = my_sol.Solution()

for x in range(1, T+1):
    S, K = _input.readline().split(' ')
    K = int(K)
    y = sol.min_flips(S, K)
    out = 'Case #{}: {}\n'.format(x, y)
    output.write( out )

_input.close()
output.close()