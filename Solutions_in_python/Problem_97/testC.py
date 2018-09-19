fin = open("./C-small-attempt0.in",'r')
fout = open("./outputC.out",'w')

case_num = int(fin.readline())

for i in range(1,case_num+1):
    inline = fin.readline()
    ii = inline.split()

    a = int(ii[0])
    b = int(ii[1])

    ans = 0;

    d=0
    temp = a
    while(temp!=0):
        temp = temp/10
        d = d+1

    for x in range(a,b):
        for j in range(1,d):
            x_j = (x/(10**j)+(x%(10**j))*(10**(d-j)))
            if(x_j<=b and x_j>x):
                ans =  ans+1

    outline = "Case #"+str(i)+": "+str(ans)+"\n"
    fout.write(outline)

fin.close()
fout.close()
