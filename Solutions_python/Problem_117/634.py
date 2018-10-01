from pprint import pprint
import sys

""" Array Operation """
def create_2d_array(h, w, init_value):
    rtn = [init_value] * (h * w)
    return rtn

def pprint_array(m, h, w):
    sys.stdout.write('*pprint*\n')
    for y in range(h):
        for x in range(w):
            sys.stdout.write("{0} ".format(get_value(y, x, m, h, w)))
        sys.stdout.write('\n')
    sys.stdout.write('*pprint*\n')

def get_value(y, x, m, h, w):
    h -= 1
    w -= 1
    if x > w or y>h:
        print "y: {0}, x: {1}".format(y, x)
        raise KeyError

    nth = (y)*(w+1) + (x+1)

    
    #print 'get: {0}'.format(m[nth-1])
    return m[nth-1]

def set_value(y, x, m, h, w, value):
    h -= 1
    w -= 1
    if x > w or y>h:
        print "y: {0}, x: {1}".format(y, x)
        raise KeyError

    nth = (y)*(w+1) + (x+1)
    m[nth-1] = value

""" Solving method """
def get_all_distinct_values(m):
    return list(set(m))

def detect_line_same_value(line ,axis, matrix, h, w):
    """
    return True or False 
    line = line number
    axis = 0 (vertical) or 1 (horizontal)
    """
    same_value_checker = lambda x, y: (x - y) == 0

    if axis:
        """ horizontal """
        line = [get_value(line, x, matrix, h, w) for x in range(w)]
        return line.count(line[0]) == len(line)
    else:
        """ vertical """
        line = [get_value(y, line, matrix, h, w) for y in range(h)]
        return line.count(line[0]) == len(line)


def fill_line_same_value(line ,axis, matrix, h, w, v):
    """
    return True or False 
    line = line number
    axis = 0 (vertical) or 1 (horizontal)
    """
    same_value_checker = lambda x, y: (x - y) == 0

    if axis:
        """ horizontal """
        line = [set_value(line, x, matrix, h, w, v) for x in range(w)]
    else:
        """ vertical """
        line = [set_value(y, line, matrix, h, w, v) for y in range(h)]


H = 1
V = 0


if __name__ == '__main__':


    """
    h, w = 3, 3
    test = create_2d_array(h, w, 100)
    get_val = lambda y, x, m: get_value(y,x,m,h,w)
    set_val = lambda y, x, m, v: set_value(y,x,m,h,w,v)
    detect_line = lambda line,axis,m:detect_line_same_value(line,axis,m,h,w)
    set_line = lambda line,axis,m,v:fill_line_same_value(line,axis,m,h,w,v)
    pprint_array(test, h, w)
    set_val(0, 1, test, 200)
    set_val(1, 2, test, 300)
    pprint_array(test, h ,w)
    print detect_line(0, V, test)
    print detect_line(1, V, test)
    print detect_line(2, V, test)
    set_line(0, V, test, 1)
    pprint_array(test, h, w)
    """

    pin = sys.stdin
    pout = sys.stdout

    cases_num = int(pin.readline().strip())

    for run_time in range(cases_num):
        h, w = pin.readline().strip().split(' ')
        h, w = int(h), int(w)
        matrix_string = ""

        for run_time_for_line in range(h):
            line = pin.readline().strip()
            matrix_string += line + " "

        matrix_string = matrix_string.strip()
        get_m_num_s = matrix_string.split(' ')
        test = [int(s) for s in get_m_num_s]

        """ test is the matrix now, and with h, w """
        get_val = lambda y, x, m: get_value(y,x,m,h,w)
        set_val = lambda y, x, m, v: set_value(y,x,m,h,w,v)
        detect_line = lambda line,axis,m:detect_line_same_value(line,axis,m,h,w)
        set_line = lambda line,axis,m,v:fill_line_same_value(line,axis,m,h,w,v)

        #pprint_array(test, h, w)

        distinct_value = get_all_distinct_values(test)

        for n,dist_value in enumerate(distinct_value):
            #print '#{0} round'.format(n)
            if n == len(distinct_value)-1:
                break
            col_to_fill = []
            row_to_fill = []
            number_to_fill = distinct_value[n+1]
            number_to_find = dist_value
            col_to_check = [x for x in range(w) if get_val(0,x,test)==number_to_find]
            row_to_check = [y for y in range(h) if get_val(y,0,test)==number_to_find]
            # col

            for col in col_to_check:
                if detect_line(col, V, test):
                    col_to_fill.append(col)
            for row in row_to_check:
                if detect_line(row, H, test):
                    row_to_fill.append(row)

            """
            print "col_to_fill"
            print col_to_fill
            print "row_to_fill"
            print row_to_fill
            """

            if not col_to_fill and not row_to_fill:
                break

            """
            set lines, then go to the next round
            """

            # set cols
            for col in col_to_fill:
                set_line(col,V,test,number_to_fill)

            # set rows
            for row in row_to_fill:
                set_line(row,H,test,number_to_fill)
        
        # check the whole matrix
        if test.count(test[0]) == len(test):
            print "Case #{0}: YES".format(run_time+1)
        else:
            print 'Case #{0}: NO'.format(run_time+1)

            



                



        
    
