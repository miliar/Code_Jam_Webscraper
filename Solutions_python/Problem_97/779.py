f = open('C-large.in', 'r')
a = open('out.txt', 'w')

for i in range(int(f.readline().strip())):
    lower, upper = [int(x) for x in f.readline().strip().split()]
    cand = set([])
    for j in range(lower,  upper+1):
        num = str(j)
        num_length = len(num)
        for k in range(1, num_length):
            curr = num[k:] + num[:k]
            if len(num)==len(curr) and int(num) != int(curr) and \
               lower <= int(curr) and int(curr) <= upper:
                if (curr, num) not in cand:
                    cand.add((num, curr))
    a.write( 'Case #'+str(i+1)+": "+str(len(cand))+"\n")
    print 'Case #'+str(i+1)+": "+str(len(cand))
	
f.close()
a.close()
