#f = open('B-small-attempt2.in', 'r')
f = open('B-large.in', 'r')
#f = open('B-sample.in', 'r')
outpu=open('output.txt','w')
cases = int(f.readline())
for case in range(cases):
    N=int(f.readline())
    A=[int(x) for x in f.readline().split(" ")]
    count=0
    while (len(A)>0):
        #print(str(A)+" "+str(count))
        minat = A.index(min(A))
        count = count + min([minat, len(A)-1-minat])
        del A[minat]        
    result = str(count)
    print('Case #'+ str(case+1)+": "+ result)
    outpu.write('Case #'+ str(case+1)+": "+ result+"\n")
f.close()
outpu.close()
