rfile = open("B-large.in.txt","r")
wfile =  open("B-large-out.txt","w+")
T = int (rfile.readline()[:-1])
for t in range(T):
    num = rfile.readline()[:-1]
    size = len(num)-1
    i=0
    #print num, '--'
    while i < size:
        if(int(num[i]) > int(num[i+1]) ):

            #print int(num[i]), int(num[i+1])
            num_int = int(num)

            factor = (10**(size-i))
            leading = (num_int/ factor)
            #print leading
            tmp_num =  leading * 10**(size - i )
            num_int = tmp_num -1
            #print num_int
            num= str(num_int)
           #print num
            size = len(num)-1
            i=0
            continue;
        i+=1
    wfile.write('Case #'+str(t+1)+': '+num+'\n')
    #print num, '--'
rfile.close()
wfile.close()