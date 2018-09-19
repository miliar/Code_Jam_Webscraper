import sys

file = open(sys.argv[1],'r')
#out = open(sys.argv[2], 'w')

numcases = int(file.readline().splitlines()[0])


cur_case = 0

while cur_case < numcases:
    cur_case += 1
    dimensao = int(file.readline().splitlines()[0])
    linha = file.readline().splitlines()[0].split(" ")
    vec1 = []
    for coord in linha:
        vec1.append(int(coord))
        
    vec1.sort()
    vec2 = []
    linha = file.readline().splitlines()[0].split(" ")
    for coord in linha:
        vec2.append(int(coord))

    vec2.sort()
    vec2.reverse()
    cur = 0
    scalar = 0
    while cur < dimensao:
        scalar += vec1[cur]*vec2[cur]
        cur += 1
        
        
    
    print "Case #" + str(cur_case)+ ": "+str(scalar) 

        
        





