
fin = open ('c:/users/hai/my projects/google code jam/2011/qualification/b/B-large.in')
fout = open ('c:/users/hai/my projects/google code jam/2011/qualification/b/B-large.out','w')

T = int(fin.readline())

for testcase in range(1,T+1):
    
    l = fin.readline().split()
    
    C = int(l[0])
    combinations_dict = {}
    for s in l[1:1+C]:
        c1,c2,c3= s
        combinations_dict[(c1,c2)] = c3
        combinations_dict[(c2,c1)] = c3

    D = int(l[C+1])
    oppose_dict = {}
    for s in l[C+2:C+2+D]:
        c1,c2 = s
        oppose_dict[(c1,c2)] = 1
        oppose_dict[(c2,c1)] = 1

    N = int(l[C+2+D])
    S = l[C+D+3]

    invoke = []
    for c in S:
        if len(invoke)==0:
            invoke.append(c)
        else:
            last = invoke[-1]
            if (last,c) in combinations_dict:
                invoke = invoke[:-1]
                invoke.append(combinations_dict[last,c])
            else:
                found_oppose = False
                for c2 in invoke:
                    if (c2,c) in oppose_dict:
                        found_oppose = True
                        break
                if found_oppose:
                    invoke = []
                else:
                    invoke.append(c)


    # output
    l_out = 'Case #' + str (testcase) + ': ['
    if len(invoke)==0:
        pass
    else:
        for i in invoke[:-1]:
            l_out += i + ', '
        l_out += invoke[-1]
    l_out += ']\n'
    fout.write(l_out)
    


fin.close()
fout.close()
