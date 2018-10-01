if __name__=='__main__':    
    input_file = open('D-large-0.in', 'r')
    output_file = open('D-large-0.out', 'w')
    
    for line_num, line in enumerate(input_file.readlines()[2::2]):
        candy = map(int, line.split())
        
        sorted_candy = sorted(candy)
        diff = 0
        for s, u in zip(sorted_candy, candy):
            if s != u:
                diff += 1
                
        print >>output_file, 'Case #%s: %f' % (line_num+1, diff)#>>output_file, 

    input_file.close()
    output_file.close()
