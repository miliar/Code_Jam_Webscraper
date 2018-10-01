googlese = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
english = ['y', 'h', 'e', 's', 'o', 'c', 'v', 'x', 'd', 'u', 'i', 'g', 'l', 'b', 'k', 'r', 'z', 't', 'n', 'w', 'j', 'p', 'f', 'm', 'a', 'q']

test = raw_input()
test = int(test)
for l in range(1, test+1):
    tex_g = raw_input()
    tex_e = ''
    k = len(tex_g)
    for i in range(0, k):
        char = tex_g[i]
        ##print "input char" + char
        for m in range(0, 26):
            if char == googlese[m]:
                tex_e = tex_e + english[m]
                ##print "output char" + tex_e
            elif char == ' ' and m == 25:
                ##print "this is space" + char
                tex_e = tex_e + ' '

    print "Case #%s: %s" %(l, tex_e)
    ##print tex_e
