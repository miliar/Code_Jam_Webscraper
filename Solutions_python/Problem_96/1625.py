import sys

def process(inputfile, outputfile):
    f = open(inputfile, 'r')
    inputdata = f.readlines()
    f.close()

    it = iter(inputdata)

    # number of cases
    N = int(it.next())
    
    fout = open(outputfile, 'w')

    for i in range(1, N+1):
        str1 = "Case #" + str(i) + ": "
        fout.write(str1)

        line = [int(digit) for digit in it.next().split()]
        
        num = line[0] # number of Googlers
        sts_max = line[1] # number of surprising triplets of scores
        p = line[2] # best result

        sts = 0 # counter of surprising triplets
        y = 0 # maximum number of Googlers who could have had...

        t = [] # list of total points of Googlers
        
        j = 0
        k = 3
        while j < num:
            t.append(line[k])
            j += 1
            k += 1
        
        for c in t:
            t1 = c/3
            is_sts = False
            if sts < sts_max:
                if t1 == 0:
                    t2 = 0
                    t3 = 0
                else:
                    t2 = p
                    t3 = c - (t1+t2)
		s1 = max(t1,t2,t3)
		s2 = min(t1,t2,t3)
                if s1 - s2 == 2:
                    is_sts = True
            if is_sts:
                sts += 1
	    elif c%3 == 0:
		t2 = t1
		t3 = t1
	    else:
		t2 = t1 + 1
		t3 = c - (t1+t2)
	    if t1 >= p or t2 >= p or t3 >= p:
		y += 1
	    #fout.write(str(t1) + ' ' + str(t2) + ' ' + str(t3) + "\n")

        fout.write(str(y) + "\n")

    fout.close()
    
def main():
    if len(sys.argv) != 3:
        print 'usage: ./dancing.py inputfile outputfile'
        sys.exit(1)

    inputfile = sys.argv[1]
    outputfile = sys.argv[2]

    process(inputfile, outputfile)

if __name__ == '__main__':
    main()
