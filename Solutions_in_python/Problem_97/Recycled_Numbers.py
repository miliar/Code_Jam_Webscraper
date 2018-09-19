#~ Recycled Numbers
def required_rotated_list_len(n, A, B):
    m = str(n)
    r = []
    for i in range(len(m)):
        m = m[-1]+m[:-1]
        if  (   n < int(m)
            and (   int(m) >= A
                and int(m) <= B
                )
            ):
            #~ print('%d, %d'%(n,int(m)))
            r.append(int(m))
    #~ print(n,r)
    return(len(list(set(r))))

f = open('C-small-attempt0.in')
for case in range(int(f.readline().strip())):
    l = f.readline().strip().split()
    A, B = int(l[0]), int(l[1])
    #~ print('>',A,B)
    print('Case #%d:'%(case+1),sum( [required_rotated_list_len(n, A, B) for n in range(A,B+1,1)] ))