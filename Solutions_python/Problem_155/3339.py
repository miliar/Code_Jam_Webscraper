# -*- coding: utf-8 -*-

input_filename  = "A-large.in"
output_filename = "A-large.out"

input_file_resource  = open  (input_filename, "r")
output_file_resource = open (output_filename, "w")

t = int (input_file_resource.readline ().strip ())
# print t

for ti in range (t):
    
    n_invite = 0

    input_line_str_array = input_file_resource.readline ().strip ().split ()
#    print input_line_str_array
    
    smax         = int (input_line_str_array[0].strip ())
    slevel_str   = input_line_str_array[1].strip ()
    slevel_array = map (int, list (slevel_str))
#    print smax
#    print slevel_str
#    print slevel_array
    
    if smax > 0:
        
#        print range (1, smax + 1)
        for k in range (1, smax + 1):
            
            klev_n_add  = 0
            klev_n_need = k
            klev_n_in   = sum (slevel_array[:k])

            if klev_n_need > klev_n_in:
                klev_n_add        = klev_n_need - klev_n_in
                slevel_array[k-1] = slevel_array[k-1] + klev_n_add
                n_invite          = n_invite + klev_n_add
            
#            print "A1 ", klev_n_need
#            print "A2" , klev_n_in
#            print "A3" , klev_n_add
            
    result_str = "Case #%s: %s\n" % (ti + 1, n_invite)
#    print result_str
    output_file_resource.write (result_str)
    


input_file_resource.close ()
output_file_resource.close ()
