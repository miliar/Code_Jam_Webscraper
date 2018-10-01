#!/usr/bin/python

def removeWrong(dict, possible_letters, pos):
    # print dict
    new_dict = []
    for word in dict:
        # print "Looking at word", word,
        if word[pos]  in possible_letters:
            # print possible_letters, "not at", pos, "in", word
        # else:
            # print possible_letters, "at", pos, "in", word
            new_dict.append(word)
    
    # print new_dict
    # print ""
    return new_dict

(L,D,N) = map(int, raw_input().split(' '))

dict = []
for x in range(0, D):
    dict.append(raw_input().strip())

for x in range(0, N):
    tmp_dict = []
    for word in dict:
        tmp_dict.append(word)
    
    data = raw_input().strip()

    pos = 0
    while data != '':
        possible_letters = []
        if data[0] == '(':
            data = data[1:]
            while data[0] != ')':
                possible_letters.append(data[0])
                data = data[1:]
            data = data[1:]
        else:
            possible_letters.append(data[0])
            data = data[1:]
            
        tmp_dict = removeWrong(tmp_dict, possible_letters, pos)
        
        pos += 1
    
    print "Case #"+str(x+1)+":",len(tmp_dict)
