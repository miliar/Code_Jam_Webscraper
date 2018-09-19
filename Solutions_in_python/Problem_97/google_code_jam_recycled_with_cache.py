def is_recycled(A,B):
    a_str = str(A)
    b_str = str(B)
    
    if a_str == b_str:
        return False
    
    convert_str = a_str
    for i,e in enumerate(a_str):
        convert_str = convert_str[1:] + convert_str[0]            
        if convert_str == b_str:
            return True
    return False
        

def num_recycled(A,B):
    counter = 0

    rec_count = 0
    for n1 in range(A,B+1):
        for n2 in range(n1 + 1,B+1):
            rec_count = rec_count + 1
            if is_recycled(n1, n2) == True:
                counter = counter + 1

    return counter

def parse_file(filename, outfile):

    f = open(filename, 'r')
    fo = open(outfile, 'w')
    num_str = f.readline()
    num = int(num_str)

    output_lines = []
    for i in range(0, num):
        line = f.readline()
        range_num = line.split()
        counter = num_recycled(int(range_num[0]), int(range_num[1]))
        
        output_str = ''
        output_str = 'Case #' + str(i+1) + ': ' + str(counter) + '\n'
        fo.write(output_str)
        output_lines.append(output_str)
    fo.close()
    

#print is_recycled(12345, 34512)
#print num_recycled(1, 9)
#print num_recycled(10, 40)
#print num_recycled(100, 500)
#print num_recycled(1111, 2222)

parse_file('C:\downloads\udacity\cs_101\input_final_recycled.in', 'C:\downloads\udacity\cs_101\output_code.txt')
