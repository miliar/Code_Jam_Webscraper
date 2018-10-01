the_input_file="A-large.in"
the_output_file="OversizedPancakeFlipper.out"

with open(the_input_file, 'r') as f:
    strings = [line.rstrip('\n') for line in f]
    
del(strings[0])
answers=[]

for pancakes in strings:
    #print ("case \n")
    p=pancakes.split()
    k=int(p[1])
    oven=list(p[0])
    length=len(oven)
    flips=0
    isPossible=True
    i=0
    while i<(length):
        if not isPossible:
            break
        if oven[i]=="-":
            flips+=1
            for j in xrange(i,i+k):
                if j<length:
                    if oven[j]=="-":
                        oven[j]="+"
                    elif oven[j]=="+":
                        oven[j]="-"
                else :
                    isPossible=False
                    break
            #print ("flipped",oven)
        else:
            i+=1
            
    if isPossible:
        answers.append(flips)
        
    else:
        answers.append("IMPOSSIBLE")
        
length=len(answers)            
with open(the_output_file, 'w') as f:
    for i in xrange (length):
        ans="Case #"+str(i+1)+": "+str(answers[i])+'\n'
        print ans
        f.write(ans)
