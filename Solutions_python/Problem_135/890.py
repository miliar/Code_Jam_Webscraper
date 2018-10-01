T = int(raw_input())

for i in range(T):
    row1 = int(raw_input())-1
    arr1 = []
    for j in range(4):
        arr1.append(raw_input())
    row2 = int(raw_input())-1
    arr2 = []
    for j in range(4):
        arr2.append(raw_input())
    list1 = map(int,arr1[row1].split())
    list2 = map(int,arr2[row2].split())
    out = []
    for num1 in list1:
        for num2 in list2:
            if num2==num1:
                out.append(num2)
    if len(out)==0:
        print "Case #"+str(i+1)+": Volunteer cheated!"
    elif len(out)==1:
        print "Case #"+str(i+1)+": "+str(out[0])
    else:
        print "Case #"+str(i+1)+": Bad magician!"
