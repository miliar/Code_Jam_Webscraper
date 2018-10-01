def get_next_num(v1):
    ret_str = v1
    val = 'a' 
    index = -1   
    for i in range(0, len(v1)-1):
        tempStr = v1[len(v1)-1 - i:]
        tempchar = v1[len(v1)-2 - i]
        
        for j in xrange(len(tempStr)):
            if tempStr[j] > tempchar and tempStr[j] < val:
                val = tempStr[j]
                index = j
                
        if index != -1:
            main_index = len(v1)-1 - i + index
            swap_index = len(v1)-2 - i
            ret_list = []
            print swap_index, main_index
            for k in xrange(len(v1)):
                if k == len(v1)-2 - i:
                    ret_list.append(v1[main_index])
                elif k == main_index:
                    ret_list.append(v1[swap_index])
                else:
                    ret_list.append(v1[k])                  
            temp2 = sorted(ret_list[swap_index+1:])
            temp3 = []
            for k in xrange(len(v1)):
                if k < swap_index+1:
                    temp3.append(ret_list[k])
                else:
                    temp3.append(temp2[k-swap_index-1])
            ret_str = ''.join(temp3)
            break
            
    if ret_str == v1:
        print v1
        ret_list = []
        temp2 = sorted(v1)
        for i in xrange(len(temp2)):
            if temp2[i] != '0':
                temp = temp2[i]
                temp2[i] = temp2[0]
                temp2[0] = temp
                break
        ret_list.append(temp2[0])
        ret_list.append('0')
        for i in range(1, len(v1)):
            ret_list.append(temp2[i])
        ret_str = ''.join(ret_list)
          
    return ret_str 
        
def prepare_input(input_file):
    test_case_count = int(input_file.readline())  #number of test cases
    
    output_file = file("B-large.out", "w")
    
    for test_case_counter in xrange(test_case_count):

        n = input_file.readline().replace('\n','') #integer count       
        
        out_put = get_next_num(n)
            
        #lowest count will be the number of switches in the server
        output_file.write("Case #"+str(test_case_counter+1)+": "+ str(out_put)+"\n") 

    output_file.close()
    
if __name__ == "__main__":
    input_file = file("B-large.in")
    prepare_input(input_file)
