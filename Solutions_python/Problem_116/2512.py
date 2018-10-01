File=open("A-large.in","rU")
f=[]
for a in File:
    f.append(a)
index=1
case = 0
while case<int(f[0]):
    inp=f[index:(index+5)]
    index+=5
    #row
    listrow = []
    list1=''
    for a in inp:
        for b in a:
            if b != '\n':
                list1=list1+b
                if len(list1) ==4:
                    listrow.append(list1)
                    list1=''
    #column
    listcol = []
    ind1=0
    ind2=0
    list1=''
    while ind2<4:
        while ind1<4:
            list1+=listrow[ind1][ind2]
            ind1+=1
            if len(list1)==4:
                listcol.append(list1)
        list1=''
        ind1=0
        ind2+=1
    #diagonal
    listdia = []
    ind=0
    list1=''
    while ind<4:
        list1+=listrow[ind][ind]
        if len(list1)==4:
            listdia.append(list1)
        ind+=1
    list1=''
    ind1=0
    ind2=3
    while ind1<4:
        list1+=listrow[ind1][ind2]
        if len(list1)==4:
            listdia.append(list1)
        ind1+=1
        ind2-=1

    #test
    test=True
    case += 1

    def testing(givenList):
        test=True
        win=""
        for a in givenList:
            wincount=0
            ind=0
            if a[0]=="T":
                win=a[1]
            if a[0]!="T":
                win=a[0]
            if win=='.':
                ind=4
            while ind<4:
                if a[ind]==win or a[ind]=="T":
                    wincount+=1
                    if wincount == 4:
                        print "Case #"+str(case)+": "+win+" won"
                        test=False
                        break
                ind+=1
        return test
    
    #row
    if test==True:
        test=testing(listrow)        

    #column
    if test==True:
        test=testing(listcol)

    #diagonal
    if test==True:
        test=testing(listdia)
    
    #not finished
    if test==True:
        list1=''
        for a in listcol:
            for b in a:
                list1+=a
        if '.' in list1:
            print "Case #"+str(case)+": Game has not completed"
            test=False
        
    #draw
    if test==True:
        print "Case #"+str(case)+": Draw"
        test=False

