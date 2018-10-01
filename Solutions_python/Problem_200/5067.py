def read_in_chunks(file_object, chunk_size=1024):
    """Lazy function (generator) to read a file piece by piece.
    Default chunk size: 1k."""
    while True:
        data = file_object.read(chunk_size)
        if not data:
            break
        yield data

def code_logic(actual_ele):
    
    while actual_ele:
        ele = actual_ele
        list_of_ele = []
        val = 1
        y = -1
        got_number = True
        
        while val:
            #print val, ele
            remainder = ele % 10
            val = ele/10
            list_of_ele.insert(0, remainder)
            ele = val
        
        #Sprint list_of_ele
        for x in list_of_ele:
            if y > x:
                got_number = False
                break
            y = x
        
        if got_number:
            return got_number, actual_ele

        actual_ele = actual_ele - 1  
        

def main_code():
    line_no = 0
    no_of_lines = -1
    fo = open("/Users/lalit_parate/Downloads/small_out.txt", "w+")
    f = open('/Users/lalit_parate/Downloads/B-small-attempt1.in')
    for piece in read_in_chunks(f):
        for single_piece in piece.split("\n"):
            if not single_piece.strip():
                continue
            else:
                single_piece = int(single_piece.strip())

            if no_of_lines == -1:
                no_of_lines = int(single_piece)
                #print "no of lines", no_of_lines
                continue
            line_no = line_no + 1
            got_number, actual_ele = code_logic(single_piece)
            if not got_number:
                continue
            outline = "Case #{line_no}: {actual_ele}".format(line_no=line_no, actual_ele=actual_ele)
            fo.write(outline + "\n")
            print outline

main_code()