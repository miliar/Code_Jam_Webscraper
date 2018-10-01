def build_double_lookup(combine, in1, in2, out):
        combine_lvl1 = combine.get(in1)
        if combine_lvl1 == None:
            combine[in1] = {in2:out}
        else:
            combine_lvl1[in2] = out

        combine_lvl1 = combine.get(in2)
        if combine_lvl1 == None:
            combine[in2] = {in1:out}
        else:
            combine_lvl1[in1] = out

def alg(raw):
    
    combine = {}
    oppose = {}
    
    for i in range(int(raw.pop(0)) ):
        (in1, in2, out) = raw.pop(0)

        build_double_lookup(combine, in1, in2, out)
            
#        combine.append(raw.pop(0))

    for i in range( int(raw.pop(0)) ):
        (in1, in2) = raw.pop(0)
        build_double_lookup(oppose, in1, in2, 1)
        
    raw.pop(0)  # the length of the input string 'line'
    line_in = raw.pop(0).strip()
    line_out = []
    magic = None
    magic_oppose = set()
    magic_test_oppose = None
    for ch in line_in:
        
#        print(str(line_out)+ " "+str(magic))
        
        did_magic = False
        
        if magic != None and magic.get(ch) != None:
            line_out.pop()
            ch = magic.get(ch)
            did_magic = True
        else:
            if magic_test_oppose != None:
#                print("ADD "+magic_test_oppose)
                magic_oppose.add(magic_test_oppose)

#        print(str(magic_test_oppose)+" "+str(magic_oppose))

        step1 = oppose.get(magic_test_oppose)
        erase = (step1 != None) and (step1.get(ch) != None)
        for opp_ch in magic_oppose:
            opp = oppose.get(opp_ch)
            if opp.get(ch) != None:
                erase = True

        if not did_magic and magic_test_oppose != None:
                magic_oppose.add( magic_test_oppose )
        magic_test_oppose = None
        
        if erase:
            line_out = []
            magic_oppose.clear()
            magic = None
        else:
            line_out.append(ch)
            magic = combine.get(ch)
#            print("new magic:"+ch+" "+str(magic))
            
            if not did_magic:
                opp = oppose.get(ch)
                if (opp != None):
                    print("DADD "+ch)
                    magic_test_oppose = ch
        
        
    print(combine)
    print(oppose)
    print(line_out)
    print(' ')
    
    return ['['+', '.join(line_out)+']']

if __name__ == '__main__':
    fname = "B"
#    f = open(fname+".in.txt", "r")
#    f = open("/home/lawford/Desktop/"+fname+"-small-attempt1.in")
    f = open("/home/lawford/Desktop/"+fname+"-large.in")
    f.readline()
    cnt=1
    fout = open(fname+".out.txt", "w")

# 1-part problem
    piece1 = f.readline()
    while piece1 != '':
        result = alg(piece1.split(' '))
        fout.write("Case #"+str(cnt)+": "+" ".join(map(str, result))+"\n")
        piece1 = f.readline()

# 2-part problem
#    piece1 = f.readline()
#    while piece1 != '':
#        num_lines = int(piece1)
#        lines = []
#        for i in range(0, num_lines*2-1):
##            [s,e] = map(int, f.readline().split(" "))
#            line = f.readline().strip()
#            print(line)
#            lines.append( map(int, line.split(" ")) )
#        result = alg(lines)
#        fout.write("Case #"+str(cnt)+": "+" ".join(map(str, result))+"\n")
#        piece1 = f.readline()

        cnt = cnt+1
    fout.close()
    f.close()
