def find_recycled(int A, int B):
    sols = set() 
    cdef int n, i, dignum
    for n from A <= n <= B: 
        digstr = str(n)
        for i from 0 <= i < len(digstr):
            digstr = digstr[1:] + digstr[0]
            dignum = int(digstr)
            if A <= dignum and dignum <= B and (n, dignum) not in sols and n != dignum:
                sols.add((n, dignum))
                sols.add((dignum, n))
    return len(sols)/2
