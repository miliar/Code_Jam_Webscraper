def chunk(data,n):
    return (data[i:i+n] for i in xrange(0,len(data),n))

def difference(current,going_to):
    if current == going_to:
        return 0
    elif current > going_to:
        return -1
    else:
        return 1
        
def process(line):
    line = line.rstrip()
    
    line_list = line.split()
    total_button_presses = int(line_list[0])
    line_list.pop(0)
    chunks = (chunk(line_list,2))
    orange_list = []
    blue_list = []
    main_list = []
    for i in chunks:
        main_list.append(i)
        if i[0] == "O":
            orange_list.append(i)
        elif i[0] == "B":
            blue_list.append(i)

        
    orange = 1
    blue = 1
    count = 0
    
    while total_button_presses != 0:
        if len(main_list) > 0:
            main_push = main_list[0]
        if main_push:
            if len(orange_list) > 0:
                orange_push = orange_list[0]
            else:
                orange_push = None
            if len(blue_list) > 0:
                blue_push = blue_list[0]
            else:
                blue_push = None
            if orange_push:
   
                difference_val = difference(int(orange),int(orange_push[1]))
                orange = orange + difference_val
                if orange_push == main_push and int(orange) == int(orange_push[1]) and int(difference_val) == 0:
                    main_list.pop(0)
                    orange_list.pop(0)
                    total_button_presses = int(total_button_presses) -1
                
            if blue_push:
                difference_val = difference(int(blue),int(blue_push[1]))
                blue = blue + difference_val
                if blue_push == main_push and int(blue) == int(blue_push[1]) and int(difference_val) == 0:
                    main_list.pop(0)
                    blue_list.pop(0)
                    total_button_presses = int(total_button_presses) -1
 
        count = count + 1
        
    return count

def main(file,output="output.out"):
    data = open(file, "rb")
    output_file = open(output, "wb")
    total = data.readline()
    count = 0
    while 1:
        lines = data.readlines(5000)
        if not lines:
            break
        output = []
        for line in lines:
            count += 1
            output_string = "Case #" + str(count) +": "+ str(process(line))
            output.append(output_string)
        for item in output:
            
            output_file.write("%s\n" % item)

if __name__ == '__main__':
    file_name = 'A-small-practice.in'
    main(file_name,'output.out')