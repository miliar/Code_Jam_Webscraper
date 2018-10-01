from sys import argv


def extract_input( filename ):
    try:
        print "Your first variable is:", filename
        file = open(filename, 'a+')
        out_file = open('out', 'a+')
        no_of_input = int(file.readline())

        case_list = []

        output_list = []

        index = 1

        for lines in file.readlines():
            line = lines.split('\n')[0]
            if lines == '\n':
                output  =('Case #%s: %s\n') %(str(index),generate_output( case_list ))
                out_file.write(output)
                case_list=[]
                index+=1
            else:
                case_list.append( line )
    except Exception as e:
        print e

def generate_output( case ):
    column1= []
    column2= []
    column3= []
    column4= []

    diagnol1 = []
    diagnol2 = []

    main_index = 0

    no_dot = True

    for row in case:
        row_list = []
        index = 0

        for column in row:
            if column == '.':
                no_dot = False
            row_list.append( column )
            if index == 0:
                column1.append( column )
            if index == 1:
                column2.append( column )
            if index == 2:
                column3.append( column )
            if index == 3:
                column4.append( column )


            if main_index%5 == 0 :
                diagnol1.append(column)
            if main_index%3 == 0 and main_index!=0 and main_index!=15:
                diagnol2.append(column)

            index+=1

            main_index+=1
        result, msg = check( row_list )
        if result:
            return msg

    result, msg = check( column1 )
    if result:
        return msg

    result, msg = check( column1 )
    if result:
        return msg

    result, msg = check( column1 )
    if result:
        return msg

    result, msg = check( column1 )
    if result:
        return msg

    result, msg = check( column2 )
    if result:
        return msg

    result, msg = check( column3 )
    if result:
        return msg

    result, msg = check( column4 )
    if result:
        return msg

    result, msg = check( diagnol1 )
    if result:
        return msg

    result, msg = check( diagnol2 )
    if result:
        return msg

    if no_dot:
        return 'Draw'
    else:
        return 'Game has not completed'



def check( test ):
    set_test = set( test )
    str_test = ''.join(set_test)
    if str_test == 'XT' or str_test=='X' or str_test=='TX':
        return ( True, 'X won' )
    if str_test=='OT' or str_test=='O' or str_test=='TO':
        return ( True, 'O won' )

    return ( False, 'Game has not completed' )




if __name__ == '__main__':
    script, filename = argv
    extract_input( filename )
