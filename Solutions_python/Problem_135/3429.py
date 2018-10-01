testcases = int(raw_input())
n=1
while n<=testcases:
    firstGuess = int(raw_input())
    configuration1 = []
    i=0
    while i<4:
        row = map(int, raw_input().split()) 
        configuration1.append(row)
        i+=1
        
    secondGuess = int(raw_input())
    i=0
    configuration2=[]
    while i<4:
        row = map(int, raw_input().split()) 
        configuration2.append(row)
        i+=1

    intersection = set(configuration1[firstGuess-1]).intersection(set(configuration2[secondGuess-1]))
    length = len(intersection)
    if(length==1):
        s =  "".join(str(e) for e in intersection)
        print("Case #%s: %s" % (n,s))
    elif(length==0):
        print("Case #%s: Volunteer cheated!" % (n))
    else:
        print("Case #%s: Bad magician!" % (n))
        
    n+=1
