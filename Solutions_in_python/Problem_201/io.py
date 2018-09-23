import ms

inp_name = 'C-small-1-attempt0.in'
out_name = 'C-small-1-attempt0.out'

_input = open(inp_name, 'r')  # small.in needs to be in the same dir as this file
output = open(out_name, 'w') # small.out will be created in this dir if it doesn't already exist

T = int( _input.readline() )

for x in range(1, T+1):
    N, K = map( int, _input.readline().split(' ') )
    y, z = ms.last_lr(N, K)
    out = 'Case #{}: {} {}\n'.format(x, y, z)
    output.write( out )

_input.close()
output.close()