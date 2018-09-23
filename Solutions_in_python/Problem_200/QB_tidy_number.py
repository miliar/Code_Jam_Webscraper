

def get_input(path):
    
    file_des = open(path)
    n  = int(file_des.readline())
    in_list = [ l.strip() for l in file_des.readlines()]
    file_des.close()
    return in_list

def get_tidy_numbers(in_list):
    if not in_list:
        print "no in list"
        return
    #print in_list
    out_list = []
    
    for num in in_list:
        dig_list  = [ch for ch in str(num)]
       # print num , dig_list
        for i in range(len(dig_list)-1, -1, -1):
            if i == 0:
                continue
            if int(dig_list[i-1]) > int(dig_list[i]):
                if int(dig_list[i-1]) == 0:
                    dig_list[i-1] = str(9)
                else:
                    dig_list[i-1] = str(int(dig_list[i-1])-1)
                j = i
                while j < len(dig_list):
                    dig_list[j] = '9'
                    j+=1
                
        if dig_list[0] == '0':
            dig_list.pop(0)
        
        out_list.append("".join(dig_list))
    return out_list

def print_output(out_list):
    if not out_list:
        print "nothing to print"
        return
    for i in range(1, len(out_list)+1):
        print "Case #{}: {}".format(i,out_list[i-1])
    
    
def main():
    
    in_list = get_input(raw_input("file path : "))
    out_list = get_tidy_numbers(in_list)
    print_output(out_list)

main()
#in_list = [132,1000,7,111111111111111110]
#print_output(get_tidy_numbers(in_list))