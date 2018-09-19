from string import*
f_input = open ( 'A-small-attempt1.in' , 'r' )
f_output = open ( 'A-small-attempt1_ans.in' , 'w' )
lines = f_input.readlines()
lines_num = int(lines[0])
lines_edited = []
case = 0
while case < lines_num:
    lines_edited.append((lines[case+1]).strip())
    line = lines_edited[case].split()
    length = int(lines_edited[case][0])
    line = lines_edited[case][2:]
    counter = 0
    f = 0
    d = 0
    cm = 0
    while counter <= length:
        if counter > cm and line[counter] != "0":
            d = counter - cm
            f = f + d
            cm = cm + f
        if counter <= cm:
            cm = cm + int(line[counter])
        counter = counter + 1
    case = case + 1
    f_output.write ("Case #%d: " %(case) + str(f) + "\n")
    
f_output.close()

    