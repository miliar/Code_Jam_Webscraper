fname = input ("Enter the name of input file(in quotes):")    #Input the name of input file here
fin = open(fname, 'r')
fout = open('out.txt','w')

a=int(fin.readline()) #read no of test case

def move(i,f,t):
    if i<f:
        if i+t<f:
            return i+t
        else:
            return f
    else:
        if i-t>f:
            return i-t
        else:
            return f

case=1

for line in fin:
    O=[]        #initialise arrays which would contain postion
    B=[]
    S=[]

    
    o_pos=1     #initialise initial positions and time
    b_pos=1
    time=0
    dt=0


    app=[x for x in line.split(' ')]        #read line
    buttons = int(app[0])                   #read no of buttons, use it in a loop to check the sequence has been completed
    for i in range(1,(2*buttons+1),2):      #create arrays for postions of O and B and the sequence they move in(i.e. S)
        S.append(app[i])
        if app[i]=="O":
            O.append(int(app[i+1]))
        else:
            B.append(int(app[i+1]))
    #print S,O,B  #This is just to check or debug
    
    while (buttons!=0):                     #while some buttons are still remaining tobe pressed
        if(S!=[]):
            if S[0]=="O":                        #if first one to move is O
                if o_pos==O[0]:
                    S.remove("O")
                    O.remove(O[0])
                    time+=1
                    buttons-=1
                    if (B!=[]):
                        if (b_pos!=B[0]):
                            b_pos = move(b_pos,B[0],1)
                else:
                    dt=abs(o_pos-O[0])     #calculate time required to move O to final position and press button
                    time+=dt
                    o_pos=O[0]                      #move O
                    if (B!=[]):
                        b_pos = move(b_pos,B[0],dt)
                #print o_pos,b_pos,time,buttons,1   #This is just to check and debug.

        if (S!=[]):
            if S[0]=="B":                        #if first one to move is O
                if b_pos==B[0]:
                    buttons-=1
                    S.remove("B")
                    B.remove(B[0])
                    time+=1
                    if (O!=[]):
                        if (o_pos!=O[0]):
                            o_pos = move(o_pos,O[0],1)
                else:
                    dt=abs(b_pos-B[0])     #calculate time required to move O to final position and press button
                    time+=dt
                    b_pos=B[0]                      #move O
                    if (O!=[]):
                        o_pos = move(o_pos,O[0],dt)
                #print o_pos,b_pos,time,buttons,0 #This is just to check and debug.
            

    b="Case #"+str(case)+":" 
    print >>fout, b,time
    case+=1

fin.close()
fout.close()
