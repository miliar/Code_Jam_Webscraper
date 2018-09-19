noT=input()
for qwerty in range(noT):

    line=raw_input().split()

    C=int(line[0])

    combine_list=[]

    for k in range(1,C+1):
        combine_list.append(line[k])

    oppose_list=[]

    D=int(line[C+1])

    for k in range(C+2,C+1+D+1):
        oppose_list.append(line[k])

    N=int(line[C+1+D+1])

    string=line[C+1+D+2]


    #input complete

    final_list=[]

    for charac in string:
        final_list.append(charac)

        #filter combinations
        if len(final_list)>1 :
        # check if -1 and -2 are in the combine list
            temp_list=sorted([final_list[-1],final_list[-2]])

            for L in combine_list:
                TEMP_list=sorted([L[0],L[1]])
                if temp_list==TEMP_list :
                    final_list.pop(-1)
                    final_list.pop(-1)

                    final_list.append(L[2])
                        
        #filter removals
        for L in oppose_list:
                if L[0] in final_list and L[1] in final_list :
                    final_list=[]
                    break
    output=""               
    output=output+"Case #%d: [" %(noT)
    for k in range(0,len(final_list)):
        if k !=len(final_list)-1 :
            output=output+str(final_list[k])+", "

        if k==len(final_list)-1:
            output=output+str(final_list[-1])

    output=output+"]"
    
    print output
