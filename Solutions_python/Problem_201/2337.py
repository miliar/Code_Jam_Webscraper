file_object  = open('C-small-2-attempt0.in', 'r')
t = (file_object.readlines())
st = int(t[0].split()[0])
file_object.close()
res=[]
for z in range(1, st + 1):
    seat, pep = (t[z].split())
    seat, pep = int(seat), int(pep)

    m=0
    p=pep
    while(p>0):
        p=int(p/2)
        m+=1
    order = pep+1-(2**(m-1))
    
    big=1
    for i in range(m-1):
        if (seat-1)%2:
            seat=int((seat-1)/2)+1
        else:
            seat=int((seat-1)/2)
            big=big*2+2**(i)-big
    
    if big<order:
        seat=seat-1
    half=int((seat-1)/2)
    if (seat-1)%2:
        res.append([half+1,half])
    else:
        res.append([half,half])

file = open('testfile3_2.txt', 'w')
for i in range(len(res)):
    file.write("Case #{}: {} {}\n".format(i+1, res[i][0],res[i][1]))
file.close()
