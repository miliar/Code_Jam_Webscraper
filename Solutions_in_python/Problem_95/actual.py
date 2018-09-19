trans = ['y', 'h', 'e', 's', 'o', 'c', 'v', 'x', 'd', 'u', 'i', 'g', 'l', 'b', 'k', 'r', 'z', 't', 'n', 'w', 'j', 'p', 'f', 'm', 'a', 'q']

file = open("b.txt","r")
raw = file.readlines()

index = 0
for txt in raw:
    if index==0:
        nl = int(txt)
        index=index+1
    else:
        eng_word = ''
        for word in txt.rstrip('\n').split(' '):
            res = ''
            for c in word:
                val = ord(c)-ord('a')
                res = res+trans[val]
            res = res+' '
            eng_word = eng_word+res
        eng_word = "Case #"+str(index)+": "+eng_word
        index=index+1
        print eng_word