def card_finder(v_answer, arrangement_str):
    import pdb
    #pdb.set_trace()
    ar = [[],[]] 
    for ca in range(0, 2):
        for cr in range (0, 4):
            new_arrangement = map(int, arrangement_str[ca][cr].split())
            new_arrangement.sort()
            ar[ca].append(new_arrangement)
    a = 0
    b = 0
    sol = 0
    while(a < 4 and b < 4):
        if ar[0][v_answer[0]][a] == ar[1][v_answer[1]][b]:
           if sol != 0: 
               return -1
           sol = ar[0][v_answer[0]][a]
           a += 1
           b += 1
        elif ar[0][v_answer[0]][a] < ar[1][v_answer[1]][b]:
           a += 1
        else:
           b += 1
    return sol

def tex_output(sol):
    if sol > 0:
        return str(sol)
    elif sol == 0:
        return "Volunteer cheated!"
    else:
        return "Bad magician!"

foo = input() 
choice = [0,0]
for i in range(0, foo):
    dog = []
    for g in range(0, 2):
        choice[g] = input() - 1
        dog.append([])
        for k in range(0, 4):
            dog[g].append(raw_input())
    
    
    print "Case #%d: %s" % (i+1, tex_output(card_finder(choice, dog)))

 
          

