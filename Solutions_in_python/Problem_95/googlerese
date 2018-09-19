input = open('C:\\Users\\Adam\\Downloads\\CodeJam\\A-small-attempt0.in', 'r')
output = open('C:\\Users\\Adam\\Downloads\\CodeJam\\outputs.out', 'w')
cases = int(input.readline())
thiscase = 1
translation_dict = {' ':' ', 'a':'y', 'b': 'h', 'c': 'e', 'd': 's',
                    'e': 'o', 'f': 'c', 'g': 'v', 'h': 'x', 'i': 'd',
                    'j': 'u', 'k': 'i', 'l': 'g', 'm': 'l', 'n': 'b',
                    'o': 'k', 'p': 'r', 'q': 'z', 'r': 't', 's': 'n',
                    't': 'w', 'u': 'j', 'v': 'p', 'w': 'f', 'x': 'm' ,
                    'y': 'a', 'z': 'q', '\n': ''}
while thiscase <= cases:
    gstring = input.readline()
    translation = ''
    for i in range(len(gstring)):
       #print translation_dict[gstring[i]]
        translation += translation_dict[gstring[i]]
    output.write('Case #' + str(thiscase) + ': ' + translation + '\n')
    thiscase += 1
    
input.close()
output.close()
