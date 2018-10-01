
def combine(x):

    fx = x[-1]
    sx = x[-2]
    
    for n, el in enumerate(comlist):
        if len(el) > 1:
             a = el[0]
             b = el[1]

             if ((fx == a) and (sx == b)) or ((fx == b)and (sx == a)):
                 x.pop()
                 x.pop()
                 x.append(comlist[n+1])

def oppose(x):

    for elem in opplist:
        first = elem[0]
        sec = elem[1]
        if (first in x) and (sec in x):
            return True
    return False
                
fi = open("input", "r")
fo = open("output", "w")

tests = int(fi.readline())
    
for test in range(tests):
    
    base = ["Q","W", "E", "R", "A", "S", "D", "F"]
    comlist = []
    opplist = []
    invlist = []
    
    line = fi.readline()

    count = 0 
    strings = line.split()

    c = int(strings[count])
    if c > 0 :
        for i in range(c):
            element = strings[i+1]  
            comlist.append(element[:-1])
            comlist.append(element[-1])
            count += 1
          
    d = int(strings[count + 1])
    if d > 0 :
        count += 1
        for i in range(d):
            opplist.append(strings[count + i+1])
            count += 1
    else:
        count += 1
    
    invlist = list(strings[-1])

    final = []

    for i in invlist:
       final.append(i)
       if len(final) > 1:
           combine(final)
           if oppose(final):
               final = []
    
    if final:
        answer = "["
        for f in final:
            answer +=  str(f) + ", "
            
        answer = answer[:-2] + "]"
    else:
        answer = "[]"

    fo.write( "Case #" + str(test+1) + ": " + answer + "\n")

fi.close()
fo.close()
