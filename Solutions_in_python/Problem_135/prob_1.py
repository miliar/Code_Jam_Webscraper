# Test

f = open('test', 'r') ;
f_write = open('result','w')

row = f.readlines() ;

num_case = int(row[0]) ;
#print('NUM', num_case)

for index in range(0, num_case) :
    case_1_row = int(row[index*10 + 1]) ;
    case_2_row = int(row[index*10 + 6]) ;  

    line_1_use = row[case_1_row + index*10 + 1] ;
    line_2_use = row[case_2_row + index*10 + 6] ;

    # parse the element
    info_1 = line_1_use.split() ;
    set_1 = set(info_1) ;

    info_2 = line_2_use.split() ;
    set_2 = set(info_2) ;

    result_set = set_1.intersection(set_2) ; 

    if len(result_set) >1 :
        final_str = "Bad magician!"

    if len(result_set) == 0 :
        final_str = "Volunteer cheated!"
        
    if len(result_set) == 1 :
        final_str = result_set.pop() ;


    pre_out = "Case #" + str(index+1) + ": " + final_str + '\n'; 
    #print(pre_out, final_str)
    f_write.write(pre_out) 