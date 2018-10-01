import os
import re
os.chdir("C:\Documents and Settings\Administrator\Desktop")
print os.listdir(".")
f=open("input.txt","r")
f1=open("output.txt","w")
n=int(f.readline()[0:-1])
for i in range(0,n):
    line=f.readline()[0:-1]
    input_case=re.split(" ",line)
    no_of_trees=int(input_case[0])
    A=int(input_case[1])
    B=int(input_case[2])
    C=int(input_case[3])
    D=int(input_case[4])
    x0=int(input_case[5])
    y0=int(input_case[6])
    M=int(input_case[7])
    X = x0
    Y = y0
    coordinate_list=[]
    coordinate_list.append([X,Y])
    for j in range(1,no_of_trees):
        X = (A * X + B) % M
        Y = (C * Y + D) % M
        coordinate_list.append([X,Y])
    print coordinate_list
    count=0
    for j in range(0,no_of_trees-2):
        for k in range(j+1,no_of_trees-1):
            for l in range(k+1,no_of_trees):
                if (coordinate_list[j][0]+coordinate_list[k][0]+coordinate_list[l][0]) % 3 == 0 and (coordinate_list[j][1] + coordinate_list[k][1] + coordinate_list[l][1]) % 3 == 0:
                    count+=1
    f1.write("Case #" + str(i+1) + ": " + str(count))
    f1.write("\n")
f.close()
f1.close()
