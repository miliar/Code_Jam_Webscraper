import math

    

f = open('consonants', 'r')
x = int(f.readline())
print x
output = ""

for ii in range(x):
    # find consonants position    
    name_n = f.readline().split(" ")
    name = name_n[0]
    print name
    n_cons = int(name_n[1])
    consonants_at = list()
    
    for j in range(len(name)-n_cons+1):
        if name[j:(j+n_cons)].find('a')==-1 and name[j:j+n_cons].find('e')==-1 and name[j:j+n_cons].find('i')==-1 and name[j:j+n_cons].find('o')==-1 and name[j:j+n_cons].find('u')==-1:
            consonants_at.append(j)
            print name[j:j+n_cons]
             
    # count substrings
    n_value = 0
    print consonants_at
    for r in range(len(name)):
        for s in range(len(name)):
            if s-r+1 >= n_cons:
                found = False
                for t in consonants_at:
                    if t >= r and t <= s and t+n_cons-1 >= r and t+n_cons-1 <= s:
                        found = True
                        #n_value += 1
                        print str(r) + " " + str(s)
                if found:
                    n_value += 1
                    found = False

    #for i in consonants_at:
    #    x = i+1
    #    y = len(name) - i - n_cons + 1
    #    n_value = n_value + (x*y)
    #n_value -= len(consonants_at) - 1
    output += "Case #" + str(ii+1) + ": " + str(n_value) + "\n"

print output      
text_file = open("consonants.txt", "w")
text_file.write(output)
text_file.close()
        
        
        
        
        