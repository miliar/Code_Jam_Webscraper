import operator

f=open('C-large.in','r')
f1=open('output.txt','w')
t=int(f.readline())
s=0
while(s<t) :
    line1 = f.readline()
    line2 = f.readline()
    no_candy = int(line1)
    #candy_values = []
    line2 = line2[:-1] + ' '
    j=0
    j0=j
    sum_val_candy = 0
    var_count = 0
    while(j<len(line2)):
        if line2[j] == ' ':
            if var_count == 0 :
                candy_xor = int(line2[j0:j])
                min = int(line2[j0:j])
            else  :
                candy_xor = operator.xor(candy_xor,int(line2[j0:j]))
                if min > int(line2[j0:j]) :
                    min = int(line2[j0:j])
            var_count = var_count + 1
            #candy_values.append(line2[j0:j])
            sum_val_candy = sum_val_candy + int(line2[j0:j])
            j0=j+1
            
        j=j+1
    #print candy_values
    final_sum = sum_val_candy - min
    output_string = "Case #"+ str(s+1) +': ' 
    if candy_xor == 0 :
        output_string = output_string + str(final_sum) + '\n'
    else :
        output_string = output_string + 'NO'+'\n'
    print output_string
    f1.write(output_string)
    s=s+1
f.close()
f1.close()