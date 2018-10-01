import sys
input_from_file=True
fout=open("G:/o.txt","w")
if input_from_file:
    f=open("G:/ab.txt","r")
else:
    f=sys.stdin
t=int(f.readline())
for i in range(t):
    N=int(f.readline())
    s=f.readline()
    list1=map(float,s.split())
    s=f.readline()
    list2=map(float,s.split())
    y=0
    counter=0
    processed=0
    win=0
    list1.sort()
    list2.sort()
    while True:
        if list1[counter]<list2[processed]:
            counter=counter+1
            win=win+1
        processed=processed+1
        if(processed>=N):
            break
    win=N-win
    c2=N-1
    processed=N-1
    w=0

    while True:
         if(list1[c2]>list2[processed]):
             c2=c2-1
             w=w+1
         processed=processed-1
         if(processed<0):
              break



    output="Case #" + str(i+1) + ": " + str(w) + " " + str(win) + "\n"
    fout.write(output)
fout.close()
f.close()



print "done"
