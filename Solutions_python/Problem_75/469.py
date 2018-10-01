import re

def solve(string):
    new_string = string[0]
    flag = 0
    for i in range(1, len(string)):
        #print i, new_string
        new_string = new_string + string[i]
        new_string, flag = combine(new_string)
        #print "flag:", flag
        if flag == 1:
            flag = 0
            #print "continue", new_string
            continue
        #print "about to delete"
        new_string = delete(new_string[:-1], string[i])

    new_string = print_string(new_string)
    return new_string

def delete(string, char):
    string = string + char
    #print "delete begin:", string
    for d in d_list:
        comp_0 = re.compile(d[0])
        comp_1 = re.compile(d[1])
        
        result_0 = comp_0.finditer(string)
        result_1 = comp_1.finditer(string)
        
        #print string
        flag_0 = flag_1 = 0
        final_result_0 = len(string)
        final_result_1 = len(string)
        for i in result_0:
            #final_result_0 = min(i.start(), final_result_0)
            #print 'final_result_0', final_result_0
            flag_0 = 1
        for i in result_1:
            #final_result_1 = min(i.start(), final_result_1)
            #print "final_result_1", final_result_1
            flag_1 = 1
                        
        if flag_0 and flag_1:
            begin = min(final_result_0, final_result_1)
            #print "before delete", string, begin, end
            string = ''
            #string = string[:begin]
            #print "after delete", string, begin, end
    #print "delete end:", string
    return string

def combine(string):
    flag = 0
    #print 'combine begins:', string
    if len(string) < 2:
        #print "string < 2:", string
        return string, flag
    for c in c_list:
        if string[-2]+string[-1] == c[0] or string[-1]+string[-2] == c[0]:
            flag = 1
            #print "combine!", string, c[1], "flag:", flag
            #print "combine ends", string[:-2]+c[1]
            return string[:-2]+c[1], flag
    #print 'combine ends:', string 
    return string, flag

def print_string(string):
    return '[' + ', '.join(string) + ']'

                
input = open('B-large.in', 'r')
output = open('magicka.out', 'w')

t = int(input.readline())
for case in range(1, t+1):
    
    line = input.readline().strip().split()
    c_list = []
    d_list = []
    offset = 1
    #print line
    if int(line[0]) != 0:
        for i in range(int(line[0])):
            c_list.append([line[i+1][:2], line[i+1][-1]])
        offset += len(c_list)
        
    if int(line[offset]) != 0:
        for i in range(int(line[offset])):
            d_list.append(line[i+1+offset])

    n = int(line[-2])
    string = line[-1]

    #print c_list, d_list, string
    
    result = solve(string)
    
    print 'Case #'+str(case)+':', result
    print
    output.write("Case #%s: %s\n" %(case, result))
