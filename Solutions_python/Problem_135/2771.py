f=open("A-small-attempt0.in", 'r')
lines=f.readlines()
f.close()

results=[]
line=0
N=eval(lines[line])       

for i in range(1, N+1):
    line+=1
    first_row_number=eval(lines[line])
    
    for j in range(1, 5):
        line+=1
        if j==first_row_number:
            first_row=list(map(eval, lines[line].split()))

    line+=1
    second_row_number=eval(lines[line])
    
    for j in range(1, 5):
        line+=1
        if j==second_row_number:
            second_row=list(map(eval, lines[line].split()))

    result="Case #" + str(i) + ": "
    doubles=[]

    for nb in first_row:
        for nb2 in second_row:
            if nb==nb2:
                doubles.append(nb)

    if len(doubles)==1:
        result+=str(doubles[0])
    elif len(doubles)==0:
        result+="Volunteer cheated!"
    else:
        result+="Bad magician!"

    result+="\n"
    print(result)
    results.append(result)
                    

f=open("o.in",'w')
f.writelines(results)
f.close()
