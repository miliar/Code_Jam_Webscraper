#fread=open('/home/think/Downloads/A-small-attempt0.in','r')
fread=open('A-large.in','r')
fwrite=open('out.txt','w')

push_time=1
total_cases=fread.readline().strip()
for i in range(int(total_cases)):
    line1 = fread.readline().strip()
    l1= line1.split()
    seq_range = int(l1[0]) * 2
    totalTime=0
    to=1
    tb=1
    j=1
    bcredit=0
    ocredit=0
    prev_token=l1[1]
    while(j<=seq_range):
        if(l1[j]=="O"):
            j=j+1 
            to = abs(int(l1[j])-to) + push_time
            if(prev_token=="O"): # checking previous token
                bcredit=bcredit + to
                totalTime = totalTime + to
            else: #previous token=B and current token="O"
                if( to > ocredit): 
                    bcredit=to - ocredit 
                    totalTime = totalTime + bcredit
                    ocredit=0
                else:
                    totalTime = totalTime + push_time
                    bcredit=push_time
            to = int(l1[j])
            prev_token="O"      
            
        else: # current token=B
            j=j+1 
            tb = abs(int(l1[j]) - tb) + push_time
            if(prev_token=="B"): # checking previous token
                ocredit=ocredit+ tb
                totalTime = totalTime + tb   
            else: #previous token=O and current token="B"
                if (tb>bcredit):
                    totalTime = totalTime + tb - bcredit
                    ocredit= tb - bcredit
                else:
                    totalTime = totalTime + push_time
                    ocredit=push_time
            tb=int(l1[j])
            prev_token="B"      


        j=j+1

    o_string="Case #"+str(i+1)+": "+str(totalTime)+"\n"
    fwrite.write(o_string)
       

    
fread.close()
fwrite.close()
