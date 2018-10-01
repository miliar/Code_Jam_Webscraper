def find(first,second):
    match=0
    
    for a in first:
        for b in second:
            #print a,b
            if a==b:
                match=match+1
                matched = a
                print "matched",matched
    if match==1:
        return str(matched)
    elif match==0:
        return "Volunteer cheated!"
    else:
        return "Bad magician!"


file=open("c:/users/rhv/Desktop/code_jam/2014/A-small-attempt0.in","r")
file1=open("c:/users/rhv/Desktop/code_jam/2014/2014_sample_out.txt","w")
m=file.readline()
i=0
l = m.split()

while i<int(l[0]):
    m1=file.readline()
    m1.split()
    m2=file.readline()
    m2.split()
    m3=file.readline()
    m3.split()
    m4=file.readline()
    m4.split()
    m5=file.readline()
    m5.split()

    n1=file.readline()
    n1.split()
    n2=file.readline()
    n2.split()
    n3=file.readline()
    n3.split()
    n4=file.readline()
    n4.split()
    n5=file.readline()
    n5.split()
    
    first_choice = int(m1)
    second_choice = int(n1)
    print first_choice,second_choice
    first_row=[]
    second_row=[]
    first_row_int=[]
    second_row_int=[]

    if first_choice==1:
        first_row=m2
    elif first_choice==2:
        first_row=m3
    elif first_choice==3:
        first_row=m4
    else:
        first_row=m5
               

    if second_choice==1:
        second_row=n2
    elif second_choice==2:
        second_row=n3
    elif second_choice==3:
        second_row=n4
    else:
        second_row=n5
        

    print first_row,second_row
    h1= first_row.split()
    h2=second_row.split()
    for e in h1:
        first_row_int.append(int(e))
    for e in h2:
        second_row_int.append(int(e))
    print first_row_int,second_row_int    
    ans = find(first_row_int,second_row_int)
    d = "Case #" + str(i+1) +": "+ans+"\n"
    file1.write(d)
    i=i+1

file.close()
file1.close()
