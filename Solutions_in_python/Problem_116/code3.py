
def prepare_input(input_file):
    T = int(input_file.readline().replace('\n',''))
        
    outFile = file("A-large.out", "w")
        
    for test_no in xrange(T):
        result_count=0
        data = []
        for i in xrange(4):
            v1 = input_file.readline().replace('\n','')
            temp = []
            
            for j in xrange(len(v1)):
                temp.append(v1[j])
            data.append(temp)

        #print data    
        input_file.readline()
        
        outFile.write("Case #" + str(test_no+1) + ": " + get_winner(data) + "\n");
        
    outFile.close()

def get_winner(data):
    for i in xrange(4):
        o_count = 0;
        x_count = 0;
        t_count = 0;
        dot_count = 0;
        old_value = 4
        for j in xrange(4):
            if (data[i][j]=='O'):
                o_count = o_count + 1;
            elif (data[i][j]=='X'):
                x_count = x_count + 1;
            elif (data[i][j]=='T'):
                t_count = t_count + 1;
            elif (data[i][j]=='.'):
                dot_count = dot_count + 1;
        ret = total_count(o_count ,t_count ,x_count ,dot_count);
        if ret == 1:
            return "O won"
        elif ret == 2:
            return "X won"
        elif ret == 3:
            old_value = 3
            

    for j in xrange(4):
        o_count = 0;
        x_count = 0;
        t_count = 0;
        dot_count = 0;
        for i in xrange(4):
            if (data[i][j]=='O'):
                o_count = o_count + 1;
            elif (data[i][j]=='X'):
                x_count = x_count + 1;
            elif (data[i][j]=='T'):
                t_count = t_count + 1;
            elif (data[i][j]=='.'):
                dot_count = dot_count + 1;
        ret = total_count(o_count ,t_count ,x_count ,dot_count);
        if ret == 1:
            return "O won"
        elif ret == 2:
            return "X won"
        elif ret == 3:
            old_value = 3
            
    o_count = 0;
    x_count = 0;
    t_count = 0;
    dot_count = 0;
    for i in xrange(4):
        if (data[i][i]=='O'):
            o_count = o_count + 1;
        elif (data[i][i]=='X'):
            x_count = x_count + 1;
        elif (data[i][i]=='T'):
            t_count = t_count + 1;
        elif (data[i][i]=='.'):
            dot_count = dot_count + 1;
    ret = total_count(o_count ,t_count ,x_count ,dot_count);
    if ret == 1:
        return "O won"
    elif ret == 2:
        return "X won"
    elif ret == 3:
        old_value = 3

    o_count = 0;
    x_count = 0;
    t_count = 0;
    dot_count = 0;
    for i in xrange(4):
        if (data[i][3-i]=='O'):
            o_count = o_count + 1;
        elif (data[i][3-i]=='X'):
            x_count = x_count + 1;
        elif (data[i][3-i]=='T'):
            t_count = t_count + 1;
        elif (data[i][3-i]=='.'):
            dot_count = dot_count + 1;
    ret = total_count(o_count ,t_count ,x_count ,dot_count);
    if ret == 1:
        return "O won"
    elif ret == 2:
        return "X won"
    elif ret == 3:
        old_value = 3

    if old_value == 3:
        return "Game has not completed"

    return "Draw"
    

def total_count(o_count ,t_count ,x_count ,dot_count):
    if (o_count+t_count==4):
        return 1;
    elif (x_count+t_count==4):
        return 2;
    elif dot_count > 0:
        return 3
    else:
        return 4;
    
if __name__ == "__main__":
    input_file = file("A-large.in")
    prepare_input(input_file)
