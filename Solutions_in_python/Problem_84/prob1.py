'''
Created on May 22, 2011

@author: abhisekpan
'''

src_file = "prob1.in"
dest_file = "prob1.out"
count = -1
case=0
rows = 0
total_rows = total_cols = 0
output_ready = False
result_list = []
out_list = []
temp_out = ""
with open(src_file, 'r') as src:
    for line in src:
        count += 1
        tokens = line.split()  
        if count > 0:
            if total_rows == rows:
                total_rows = int(tokens[0])
                total_cols = int(tokens[1])
                result_list = [[0] * total_cols for x in xrange(total_rows)]
                rows = 0
                case += 1
            else:
                for i in xrange(total_cols):
                    result_list[rows][i] = tokens[0][i]
                rows += 1
                if total_rows == rows:
                    possible=True
                    temp_out = ""
                    for i in xrange(rows):
                        for j in xrange(total_cols):
                            if result_list[i][j] == '#':
                                if i==(rows - 1) or j==(total_cols - 1):
                                    possible=False
                                    break
                                if result_list[i][j+1] != '#':
                                    possible=False
                                    break
                                if result_list[i+1][j] != '#':
                                    possible=False
                                    break
                                if result_list[i+1][j+1] != '#':
                                    possible=False
                                    break
                                result_list[i][j] = result_list[i+1][j+1] = '/'
                                result_list[i][j+1] = result_list[i+1][j] = '\\'
                            temp_out = temp_out + result_list[i][j]
                        temp_out = temp_out + "\n"      
                    out_list.extend(["Case ", "#", str(case), ": ", "\n"])  
                    if possible==False:
                        out_list.extend(["Impossible", "\n"])       
                    else:
                        out_list.extend([temp_out])      
 
output_string = "".join(out_list)
with open(dest_file, 'w') as dest:
    dest.write(output_string.rstrip("\n"))
print "done"        