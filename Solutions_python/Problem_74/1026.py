## Written by Nivvedan S
## Google Codejam


INPUT_FILE_NAME="a.in"
OUTPUT_FILE_NAME="a.out"
IN = open(INPUT_FILE_NAME, "r")
OUT = open(OUTPUT_FILE_NAME, "w")

par_input=IN.readlines()

T=int(par_input[0].strip())
par_input=par_input[1:]

count=0
for line in par_input:
    to_parse=line.strip()
    to_parse=to_parse.split()
    N=int(to_parse[0])
    to_parse=to_parse[1:]

    Orange=[]
    Blue=[]
    Order=[]
    
    for i in range(N):
        if (to_parse[0]=="O"):
            Orange.append(int(to_parse[1]))
            Order.append("O")
        else:
            Blue.append(int(to_parse[1]))
            Order.append("B")
        to_parse=to_parse[2:]

    time=0
    b_pos=1
    o_pos=1
    while(not(Order==[])):
        pushed=False
        if not (Blue==[]):
            if not b_pos == Blue[0]:
                b_pos=b_pos+(Blue[0]-b_pos)/abs(Blue[0]-b_pos)
            elif(Order[0]=="B"):
                pushed=True
                Blue=Blue[1:]
        if not (Orange==[]):    
            if not o_pos == Orange[0]:
                o_pos=o_pos+(Orange[0]-o_pos)/abs(Orange[0]-o_pos)
            elif(Order[0]=="O"):
                pushed=True
                Orange=Orange[1:]

        if(pushed):
            Order=Order[1:]

        time=time+1
    count=count+1
    print "Case #"+str(count)+": "+str(time)
