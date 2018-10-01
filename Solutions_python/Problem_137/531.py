def sort(rows, columns, mines):
    if rows==1:
        if columns==1:
            if mines==0:
                return 'c'
            elif mines==1:
                return 'Impossible'
        elif columns==2:
            if mines==0:
                return 'c.'
            elif mines==1:
                return 'c*'
            elif mines==2:
                return 'Impossible'
        elif columns==3:
            if mines==0:
                return 'c..'
            elif mines==1:
                return 'c.*'
            elif mines==2:
                return 'c**'
            elif mines==3:
                return 'Impossible'
        elif columns==4:
            if mines==0:
                return 'c...'
            elif mines==1:
                return 'c..*'
            elif mines==2:
                return 'c.**'
            elif mines==3:
                return 'c***'
            elif mines==4:
                return 'Impossible'
        elif columns==5:
            if mines==0:
                return 'c....'
            elif mines==1:
                return 'c...*'
            elif mines==2:
                return 'c..**'
            elif mines==3:
                return 'c.***'
            elif mines==4:
                return 'c****'
            elif mines==5:
                return 'Impossible'
    elif rows==2:
        if columns==2:
            if mines==0:
                return 'c.\n..'
            elif mines==1:
                return 'Impossible'
            elif mines==2:
                return 'Impossible'
            elif mines==3:
                return 'c*\n**'
            elif mines==4:
                return 'Impossible'
        elif columns==3:
            if mines==0:
                return 'c..\n...'
            elif mines==1:
                return 'Impossible'
            elif mines==2:
                return 'c.*\n..*'
            elif mines==3:
                return 'Impossible'
            elif mines==4:
                return 'Impossible'
            elif mines==5:
                return 'c**\n***'
            elif mines==6:
                return 'Impossible'
        elif columns==4:
            if mines==0:
                return 'c...\n....'
            elif mines==1:
                return 'Impossible'
            elif mines==2:
                return 'c..*\n...*'
            elif mines==3:
                return 'Impossible'
            elif mines==4:
                return 'c.**\n..**'
            elif mines==5:
                return 'Impossible'
            elif mines==6:
                return 'Impossible'
            elif mines==7:
                return 'c***\n****'
            elif mines==8:
                return 'Impossible'
        elif columns==5:
            if mines==0:
                return 'c....\n.....'
            elif mines==1:
                return 'Impossible'
            elif mines==2:
                return 'c...*\n....*'
            elif mines==3:
                return 'Impossible'
            elif mines==4:
                return 'c..**\n...**'
            elif mines==5:
                return 'Impossible'
            elif mines==6:
                return 'c.***\n..***'
            elif mines==7:
                return 'Impossible'
            elif mines==8:
                return 'Impossible'
            elif mines==9:
                return 'c****\n*****'
            elif mines==10:
                return 'Impossible'
    elif rows==3:
        if columns==3:
            if mines==0:
                return 'c..\n...\n...'
            elif mines==1:
                return 'c..\n...\n..*'
            elif mines==2:
                return 'Impossible'
            elif mines==3:
                return 'c..\n...\n***'
            elif mines==4:
                return 'Impossible'
            elif mines==5:
                return 'c.*\n..*\n***'
            elif mines==6:
                return 'Impossible'
            elif mines==7:
                return 'Impossible'
            elif mines==8:
                return 'c**\n***\n***'
            elif mines==9:
                return 'Impossible'
        elif columns==4:
            if mines==0:
                return 'c...\n....\n....'
            elif mines==1:
                return 'c...\n....\n...*'
            elif mines==2:
                return 'c...\n....\n..**'
            elif mines==3:
                return 'c..*\n...*\n...*'
            elif mines==4:
                return 'c...\n....\n****'
            elif mines==5:
                return 'Impossible'
            elif mines==6:
                return 'c.**\n..**\n..**'
            elif mines==7:
                return 'Impossible'
            elif mines==8:
                return 'c.**\n..**\n****'
            elif mines==9:
                return 'Impossible'
            elif mines==10:
                return 'Impossible'
            elif mines==11:
                return 'c***\n****\n****'
            elif mines==12:
                return 'Impossible'
        elif columns==5:
            if mines==0:
                return 'c....\n.....\n.....'
            elif mines==1:
                return 'c....\n.....\n....*'
            elif mines==2:
                return 'c....\n.....\n...**'
            elif mines==3:
                return 'c...*\n....*\n....*'
            elif mines==4:
                return 'c...*\n....*\n...**'
            elif mines==5:
                return 'c....\n.....\n*****'
            elif mines==6:
                return 'c..**\n...**\n...**'
            elif mines==7:
                return 'c..**\n...**\n..***'
            elif mines==8:
                return 'Impossible'
            elif mines==9:
                return 'c.***\n..***\n..***'
            elif mines==10:
                return 'Impossible'
            elif mines==11:
                return 'c.***\n..***\n*****'
            elif mines==12:
                return 'Impossible'
            elif mines==13:
                return 'Impossible'
            elif mines==14:
                return 'c****\n*****\n*****'
            elif mines==15:
                return 'Impossible'
    elif rows==4:
        if columns==4:
            if mines==0:
                return 'c...\n....\n....\n....'
            elif mines==1:
                return 'c...\n....\n....\n...*'
            elif mines==2:
                return 'c...\n....\n....\n..**'
            elif mines==3:
                return 'c...\n....\n...*\n..**'
            elif mines==4:
                return 'c...\n....\n....\n****'
            elif mines==5:
                return 'c...\n....\n...*\n****'
            elif mines==6:
                return 'c...\n....\n..**\n****'
            elif mines==7:
                return 'c..*\n...*\n...*\n****'
            elif mines==8:
                return 'c..*\n...*\n..**\n****'
            elif mines==9:
                return 'Impossible'
            elif mines==10:
                return 'c..*\n...*\n****\n****'
            elif mines==11:
                return 'Impossible'
            elif mines==12:
                return 'c.**\n..**\n****\n****'
            elif mines==13:
                return 'Impossible'
            elif mines==14:
                return 'Impossible'
            elif mines==15:
                return 'c***\n****\n****\n****'
            elif mines==16:
                return 'Impossible'
        elif columns==5:
            if mines==0:
                return 'c....\n.....\n.....\n.....'
            elif mines==1:
                return 'c....\n.....\n.....\n....*'
            elif mines==2:
                return 'c....\n.....\n.....\n...**'
            elif mines==3:
                return 'c....\n.....\n.....\n..***'
            elif mines==4:
                return 'c...*\n....*\n....*\n....*'
            elif mines==5:
                return 'c....\n.....\n.....\n*****'
            elif mines==6:
                return 'c...*\n....*\n...**\n...**'
            elif mines==7:
                return 'c....\n.....\n...**\n*****'
            elif mines==8:
                return 'c..**\n...**\n...**\n...**'
            elif mines==9:
                return 'c..**\n...**\n...**\n..***'
            elif mines==10:
                return 'c....\n.....\n*****\n*****'
            elif mines==11:
                return 'c..**\n...**\n...**\n*****'
            elif mines==12:
                return 'c..**\n...**\n..***\n*****'
            elif mines==13:
                return 'Impossible'
            elif mines==14:
                return 'c..**\n...**\n*****\n*****'
            elif mines==15:
                return 'Impossible'
            elif mines==16:
                return 'c.***\n..***\n*****\n*****'
            elif mines==17:
                return 'Impossible'
            elif mines==18:
                return 'Impossible'
            elif mines==19:
                return 'c****\n*****\n*****\n*****'
            elif mines==20:
                return 'Impossible'
    elif rows==5:
        if columns==5:
            if mines==0:
                return 'c....\n.....\n.....\n.....\n.....'
            elif mines==1:
                return 'c....\n.....\n.....\n.....\n....*'
            elif mines==2:
                return 'c....\n.....\n.....\n.....\n...**'
            elif mines==3:
                return 'c....\n.....\n.....\n.....\n..***'
            elif mines==4:
                return 'c....\n.....\n.....\n....*\n..***'
            elif mines==5:
                return 'c....\n.....\n.....\n.....\n*****'
            elif mines==6:
                return 'c....\n.....\n.....\n....*\n*****'
            elif mines==7:
                return 'c....\n.....\n.....\n...**\n*****'
            elif mines==8:
                return 'c....\n.....\n.....\n..***\n*****'
            elif mines==9:
                return 'c....\n.....\n....*\n..***\n*****'
            elif mines==10:
                return 'c....\n.....\n.....\n*****\n*****'
            elif mines==11:
                return 'c....\n.....\n....*\n*****\n*****'
            elif mines==12:
                return 'c....\n.....\n...**\n*****\n*****'
            elif mines==13:
                return 'c....\n.....\n..***\n*****\n*****'
            elif mines==14:
                return 'c...*\n....*\n...**\n*****\n*****'
            elif mines==15:
                return 'c....\n.....\n*****\n*****\n*****'
            elif mines==16:
                return 'c..**\n...**\n...**\n*****\n*****'
            elif mines==17:
                return 'c..**\n...**\n..***\n*****\n*****'
            elif mines==18:
                return 'Impossible'
            elif mines==19:
                return 'c..**\n...**\n*****\n*****\n*****'
            elif mines==20:
                return 'Impossible'
            elif mines==21:
                return 'c.***\n..***\n*****\n*****\n*****'
            elif mines==22:
                return 'Impossible'
            elif mines==23:
                return 'Impossible'
            elif mines==24:
                return 'c****\n*****\n*****\n*****\n*****'
            elif mines==25:
                return 'Impossible'

def rotate(row, column, name):
    res = ''
    for n in range(0,column):
	    for m in range(0,row):
		    res += name[m*(column+1)+n]
	    res+='\n'
    return res[:-1]

def case(rows, columns, mines):
    if columns>=rows:
        n = sort(rows, columns, mines)
    else:
        n = sort(columns, rows, mines)
        if n!='Impossible':
            n = rotate(columns, rows, n)
    return n

file = open('C:\Documents and Settings\davos\Local Settings\Temp\C-small-attempt0.in.txt')
global iterations
iterations = int(file.readline())

def getLine():
    temp = file.readline().split()
    return [int(temp[0]),int(temp[1]),int(temp[2])]

def out():
    global iterations
    output = open('C:\Documents and Settings\davos\Local Settings\Temp\C-small-attempt0.out','w')
    kwrite = ''
    count = 1
    while iterations!=0:
        n = getLine()
        iterations -= 1
        print(iterations)
        kwrite = kwrite + 'Case #' + str(count) + ':\n' + str(case(n[0],n[1],n[2])) + '\n'
        count += 1
    output.write(kwrite)








            


            
