txt = open("A-large.in")
txt2 = open("A-large.out",'w')
count=int(txt.readline())
for i in range(0,count):
    mystr= txt.readline().split(" ")
    maxShy=int(mystr[0])
    audience=mystr[1]
    audienceInt=[]
    for character in audience:
        if(character!='\n'):
            audienceInt.append(int(character))
    exist=0
    friends=0
    for index,num in enumerate(audienceInt):
        if(index>exist and num!=0):
            friends = friends + (index-exist)
            exist = exist  + (index-exist)
        exist = exist + num
    txt2.write("Case #"+str(i+1)+": "+str(friends)+"\n")