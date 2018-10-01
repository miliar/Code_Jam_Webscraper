with open('cj1in.txt') as f:
    i=0
    for line in f:
        if i>0:
            seen = 0
            needed = 0
            j=0
            for char in line.split()[1]:
                if int(char) > 0 and seen<j:
                    needed = max(needed, j-seen)
                seen+=int(char) 
                j=j+1
            print 'Case #'+str(i)+': '+str(needed)
        i=i+1