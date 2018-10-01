dict = {}
dict['a'] = 'y'
dict['b'] = 'h'
dict['c'] = 'e'
dict['d'] = 's'
dict['e'] = 'o'
dict['f'] = 'c'
dict['g'] = 'v'
dict['h'] = 'x'
dict['i'] = 'd'
dict['j'] = 'u'
dict['k'] = 'i'
dict['l'] = 'g'
dict['m'] = 'l'
dict['n'] = 'b'
dict['o'] = 'k'
dict['p'] = 'r'
dict['q'] = 'z'
dict['r'] = 't'
dict['s'] = 'n'
dict['t'] = 'w'
dict['u'] = 'j'
dict['v'] = 'p'
dict['w'] = 'f'
dict['x'] = 'm'
dict['y'] = 'a'
dict['z'] = 'q'
dict [' '] = ' '
input_file = open('A-small-attempt5.in')
output_file = open('A-small-attempt0.out', 'w')



i = 0
for line in input_file:
        if (i == 0):
            cases = int(line)
            i+=1
        else:
            out = ''
            for c in line.strip('\n'):
                out += dict[c]
            output_file.write("Case #" + str(i-1) + ": "+out)
            if (i == cases+1):
                pass
            else:
                output_file.write('\n')
        i+=1
input_file.close()
output_file.close()
