import sys

file = open(sys.argv[1],'r')
out = open(sys.argv[2], 'w')

numcases = int(file.readline().splitlines()[0])



cur_case = 0

while cur_case < numcases:
    cur_case += 1

    numengines = int(file.readline().splitlines()[0])
    cur_engine = 0
    dic_engine = {}
    
    while cur_engine < numengines :
        cur_engine += 1
        dic_engine[file.readline().splitlines()[0]] = []
    
    num_queries = int(file.readline().splitlines()[0])
    cur_query = 0
    while cur_query < num_queries:
        dic_engine[file.readline().splitlines()[0]].append(cur_query)
        cur_query += 1
        

    cur_pos = 0
    num_changes = -1
    finish = False
    while not finish:
        num_changes += 1
        maior = None
        maiorItem = 0
        for eng in dic_engine:
            while (not len(dic_engine[eng]) == 0) and dic_engine[eng][0] < cur_pos:
                dic_engine[eng].pop(0)
            if len(dic_engine[eng]) == 0:
                finish = True
                break
        if finish:
            break
        for eng in dic_engine:
            a = dic_engine[eng][0]  
            if a > maiorItem:

                maiorItem = a
                cur_pos = a
                   
                
                
                

        

    print "Case #" + str(cur_case) +": " + str(num_changes)
    out.write("Case #" + str(cur_case) +": " + str(num_changes)+"\n")
        





