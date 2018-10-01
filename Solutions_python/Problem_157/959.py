__author__ = 'Giannis'
import time
f = open("C-small-attempt1.in", 'r')
s = open("Text-C.out", "w")
multiplytable = {
    'ij': 'k',
    'ik': '-j',
    'ji': '-k',
    'jk': 'i',
    'ki': 'j',
    'kj': '-i',
}

c = time.time()
def do_quat(inp):        
    if inp[0] == inp[1]:
        inp = '-1'
    else:
        if inp[0] == '1':
            inp = inp[1]
        elif inp[1] == '1':
            inp = inp[0]
        else:
            inp = multiplytable[inp]
    return inp

for t in range(int(f.readline())):
    L, R = f.readline().split()
    part = f.readline().strip()
    #print part
    #print "OK3"
    complete = "".join(part for i in range(int(R)))
    #print "Ok4"
    #print complete
    while len(complete) > 3:
        #print "R", complete
        backup = complete
        new_c = ""
        s_p = 0
        if complete.count('-') % 2 == 0:
            complete = complete.replace('-', '')
            
        else:
            complete = complete.replace('-', '')
            new_c = '-'
        
        complete = complete.replace('1', '')
        try:
            if complete[s_p] == 'i':
                complete = complete.replace('i', '', 1)
                new_c = new_c + 'i'
                if complete[s_p] == 'j':
                    complete = complete.replace('j', '', 1)
                    new_c = new_c + 'j'
                    if complete[s_p] == 'k':
                        complete = complete.replace('k', '', 1)
                        new_c = new_c + 'k'
        except:
            pass
        try:
            #print complete, complete[s_p:s_p+2], complete[s_p+2:]
            new_c = new_c + do_quat(complete[s_p:s_p+2]) 
            if 'ijk' in new_c:
                a = complete[s_p+2:]
                for q in multiplytable:
                    a = a.replace(q, multiplytable[q])
                new_c = new_c + a
            else:
                new_c = new_c + complete[s_p+2:]
                
                
        except:
            new_c = new_c + complete
        
        complete = new_c
        if complete == '-ijk' or complete == backup:
            break
    print t+1
            
    if complete == 'ijk':
        m = "Case #%d: YES\n" % (t+1)
        s.write(m)
    else:
        m = "Case #%d: NO\n" % (t+1)
        s.write(m)
    #raw_input()
print time.time() - c
f.close()
s.close()
