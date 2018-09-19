import sys

fin = open(sys.argv[1],'r')
fout = open(sys.argv[1]+".out", 'w')
case_number = 1
lines = fin.readlines()
l,d,n = int(lines[0].rsplit(" ")[0]),int(lines[0].rsplit(" ")[1]),int(lines[0].rsplit(" ")[2])

known_words = []
for i in lines[1:int(d)+1]:
    known_words.append(i[:-1])

for line in lines [int(d)+1:]:
    #print case_number
    token_list = []
    par_open = False
    temp_list = []
    for c in line:
        if c == '(':
            par_open = True
        elif c >= 'a' and c <= 'z':

            if par_open == False:
                token_list.append(c)
            else:
                temp_list.append(c)

        elif c == ')':
            par_open = False
            if len(temp_list)>0:
                token_list.append(temp_list)
            temp_list = []

    #print known_words
    #print token_list
    posibilities = 0
    misses = 0
    for kw in known_words:
        for i,c in enumerate(kw):
            if c not in token_list[i]:
                
                misses += 1
                posible = False
                break

    posibilities = d-misses
    #print case_number, d-misses

    fout.write( 'Case #%i: %s\n' %(case_number, posibilities))
    case_number= case_number + 1
            