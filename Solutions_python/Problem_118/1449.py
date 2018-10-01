infile = file('C-small-attempt0.in','r')
outfile = file('outC.txt','w')

def fq_num(min,max,fairq):
    counter = 0
    for fq in fairq:
        if fq >= min and fq <= max:
            counter += 1
    return counter

fair_sq = []
fair_sq.append(1)
fair_sq.append(4)
fair_sq.append(9)
fair_sq.append(121)
fair_sq.append(484)

num_cases = int(infile.readline())

for i in range(num_cases):
    interval = infile.readline().split()
    min = int(interval[0])
    max = int(interval[1])
    outfile.write('Case #' + str(i+1) + ': ' + str(fq_num(min,max,fair_sq)) + '\n')

infile.close()
outfile.close()
    