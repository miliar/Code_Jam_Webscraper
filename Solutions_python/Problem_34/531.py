# Filename: Alien_Language.py

# Open file
f_input = open(r'D:\googlejam\2009\A-small-attempt0.in')

# Get numbers
firstline = f_input.readline()
alist = firstline.split(' ')

L = int(alist[0])
D = int(alist[1])
N = int(alist[2])

# Get words
words=[]
for i in range(0, D):
    word = f_input.readline()
    words.append(word)
    
# Get cases
cases=[]
for i in range(0, N):
    patten = f_input.readline()
    cases.append(patten)

# Calculate cases
for i in range(0, N):
    # Copy word list
    wordList = words[:]
    
    # Get patten list
    pList = []
    patten = cases[i]
    pLen = len(patten)
    group = False
    ok = False
    result = 0
    wc = 0
    for j in range(0, pLen):
        
        token = patten[j]
        # Set flag
        if token =='(':
            group = True
            continue
        elif token ==')':
            group = False
        elif token =='\n':
            continue
            
        # Biuld List
        if not group:
            if(token != ')'):
                pList.append(token)
            ok = True
        else:
            pList.append(token)
        # Match patten
        if ok:
            #print('pList:',pList)
            for word in words:
                if (word[wc] not in pList) and (word in wordList):
                    del wordList[wordList.index(word)]
                #print(wordList)
            wc+=1
            pList=[]
            ok = False
    print('Case #%d: %d'%(i+1, len(wordList)))

f_input.close
                    

                    
        


    
    
    




