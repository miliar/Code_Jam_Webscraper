import sys
 
MODULU = 10000
        
def make_c2i (s):
    c2i = {}
    for ind,char in enumerate(s):
        c2i.setdefault(char, []).append(ind)
    return c2i

needle = "welcome to code jam"
needle_c2i = make_c2i(needle)  

def count_subs(hay):
    hay_c2i = make_c2i(hay)
    hay_stuff = []
    for hay_ind,c in enumerate(hay):
        #print hay_stuff
        hay_stuff.append({})
        #print c, needle_c2i.get(c,[])
        for needle_ind in needle_c2i.get(c,[]):
            if needle_ind == 0:
                hay_stuff[-1][0] = 1
            else:
                c_before = needle[needle_ind-1]  
                count = 0
                for c_bef_hay_ind in hay_c2i.get(c_before,[]):
                    #print needle_ind,c_before,c_bef_hay_ind
                    if c_bef_hay_ind > hay_ind:
                        break
                    assert c_bef_hay_ind < hay_ind
                    count += hay_stuff[c_bef_hay_ind].get(needle_ind-1, 0)
                    count %= MODULU
                hay_stuff[-1][needle_ind] = count
    return sum([x.get(len(needle)-1,0) for x in hay_stuff] )

def read_file(filename):
    with open(filename) as f:
        n = int(f.readline().strip())        
        for i in range(n):
            s = f.readline().strip()
            print "Case #%d: %04d" % (i + 1, count_subs(s))

            
read_file(sys.argv[1])            