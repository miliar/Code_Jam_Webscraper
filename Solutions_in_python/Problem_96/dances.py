#!/usr/bin/python 

def cutoff( n ):
    return n+(n-2)+(n-2)

f = open("data.txt")
iters = None
specials = None
count = 0 
total = 0 

for line in f: 
    if not iters:
        iters = int(line)
        continue
    #endif

    count = count+1

    dancers = None
    specials = None
    flag = None
    total = 0
    for score in line.split(" "):
        if dancers is None:
            dancers = int(score)
            #print "There are " + str(dancers) + " dancers"
            continue
        #end if 
        if specials is None :
            specials = int(score)
            #print "There are " + str(specials) + " specal scores"
            continue 
        #end if 
        if flag is None:
            flag = int(score)
            #print "The flag score is " + str(flag) + " dancers"
            continue
        #end if 

        score = int(score)
        #print "Checking score: " + str(score)
        if(score < flag):
            #print "Score is too low to even work" 
            continue 
        if score >= cutoff(flag)+2:
            #print "Score above the total (no special needed)"
            total = total+1 
        elif (score >= cutoff(flag)) and (specials > 0):
            #print "Score used a special (specials left: "+ str(specials) + ")"
            total = total+1
            specials = specials-1         
        #end if 
    #end for 
    print "Case #" + str(count) + ": " + str(total)

#end for
