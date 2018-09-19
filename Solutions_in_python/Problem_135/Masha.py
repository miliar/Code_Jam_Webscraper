def read(f):
    ind=int(f.readline())
    a=[]
    for i in range(4):
        a.append(set(map(int,f.readline().split())))
    return ind,a
file_name="A-small-attempt0.in"
fout=open("output.txt","w")
with open(file_name) as f:
    for q in range(int(f.readline())):
        ans1,a=read(f)
        ans2,b=read(f)
        fout.write('Case #%d: ' % (q+1))
        ans=a[ans1-1] & b[ans2-1]
        if not len(ans):
            fout.write("Volunteer cheated!\n")
        elif len(ans)>1:
            fout.write("Bad magician!\n")
        else:
            fout.write("%d\n" % ans.pop())