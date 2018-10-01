input_str1 = "ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv"
output_str1 = "our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up"

def parse_sample(input_str, output_str):
    code_map = {}
    for i,e in enumerate(input_str1):
        code_map[e] = output_str1[i]
    code_map['z'] = 'q'
    code_map['q'] = 'z'
    return code_map

def map_input(code_map, input_str):
    output_str = ''
    for e in input_str:
        if e in code_map:
            output_str = output_str + code_map[e]
    return output_str

def parse_file(filename, outfile):

    code_map = parse_sample(input_str1, output_str1)
    f = open(filename, 'r')
    fo = open(outfile, 'w')
    num_str = f.readline()
    num = int(num_str)

    output_lines = []
    for i in range(0, num):
        line = f.readline()
        output_str = map_input(code_map, line)
        output_str = 'Case #' + str(i+1) + ': ' + output_str + '\n'
        fo.write(output_str)
        output_lines.append(output_str)
    fo.close()
    
code_map = parse_sample(input_str1, output_str1)
print len(code_map)
for e in sorted(code_map):
    print e

for e in sorted(code_map.values()):
    print e

parse_file('C:\downloads\udacity\cs_101\input_final.in', 'C:\downloads\udacity\cs_101\output_code.txt')
