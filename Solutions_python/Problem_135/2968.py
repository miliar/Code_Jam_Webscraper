INPUT = "A-small-attempt0.in"
OUTPUT = "A-small-attempt0.out"

if __name__ == '__main__':
    in_file = file(INPUT, "r")
    out_file = file(OUTPUT, "w")
    
    lines = in_file.readlines()
    cases_num = int(lines[0])
    
    out_lines = []
    
    i = 0
    while i < cases_num:
        first_answer = int(lines[10 * i + 1])
        second_answer = int(lines[10 * i + 6])
        
        first_row = lines[10 * i + 1 + first_answer]
        first_row = first_row.strip().split(" ")
        first_row = [int(x) for x in first_row]
        
        second_row = lines[10 * i + 6 + second_answer]
        second_row = second_row.strip().split(" ")
        second_row = [int(x) for x in second_row]
        
        first_set = set(first_row)
        second_set = set(second_row)
        
        res = first_set & second_set        
        
        if len(res) == 1:
            result = "case #%d: %d\n" % (i+1,list(res)[0])
        if len(res) > 1:
            result = "case #%d: Bad magician!\n" % (i+1)
        if (len(res) == 0):
            result = "case #%d: Volunteer cheated!\n" % (i+1)
        
        out_lines += result
        i+=1
    
    out_file.writelines(out_lines)
    in_file.close()
    out_file.close()
    print 'done'
        