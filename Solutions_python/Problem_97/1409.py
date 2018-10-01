f = open("C-small-attempt0.in", 'r')
f1 = open("recycled.out", 'w')
num = int(f.readline())
count = 0

for i in f:
    count+=1
    i = i.rstrip('\n')
    ls = i.split()
    lt = []
    A = int(ls[0])
    B = int(ls[1])
    for num in range(A, B+1):
        st = str(num)
        size = len(st)
        for n in range(size-1):
            st = st[-1]+st[0:size-1]
            nm = int(st)
            if nm == num:
                continue
            if A <=nm<=B:
                at = [num, nm]
                at.sort()
                if not (at in lt):
                    lt.append(at)
    f1.write("Case #"+str(count)+": "+str(len(lt))+"\n")
    
    
