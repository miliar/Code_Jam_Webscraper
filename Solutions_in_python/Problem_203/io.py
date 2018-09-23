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
    R, C = map(int, _input.readline().split(' '))
    m_in = []
    for r in range(R):
        row_str_in = _input.readline().strip()
        m_in.append(row_str_in)
    m_out = my_sol.initialize_cake(m_in, R, C)
    out = 'Case #{}:\n'.format(x)
    output.write( out )
    for row_str_out in m_out:
        output.write(row_str_out+'\n')

_input.close()
output.close()