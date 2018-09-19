file=open("magic.txt","r")
m = int(file.readline().strip())
c=1
while m!=0:
    grid1 = []
    grid2 = []
    for i in range(0,5): 
        grid1.append(file.readline().strip())
    for i in range(0, 5):
        grid2.append(file.readline().strip())

    num1 = int(grid1[0])

    row1=grid1[num1].split()

    num2 = int(grid2[0])

    row2 = grid2[num2].split()

    a =set(row1) & set(row2)

    
        
    if len(a)>1:
        print('case #',end='')
        print(c,end=': ')
        print('Bad magician!')
    elif len(a)==1:
        print('case #',end='')
        print(c,end=': ')
        print(a.pop())
    elif len(a)==0:
        print('case #',end='')
        print(c,end=': ')
        print('Volunteer cheated!')
    c=c+1
    m=m-1
    
