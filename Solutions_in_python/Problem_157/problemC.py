# Usage : run the python interpreter. Then type :
#         import problemC
#         problemC.main("path1", "path2")
#
# path1 is the path to the input file, path2 is the path to the output file
# open the output file and enjoy the result

i=0
j=2
k=3
mi=4
mj=6
mk=7

def mult(a,b):
    if a==1:
        return b
    if b==1:
        return a
    if a == b:
        return 5
    if a==i:
        if b==j:
            return k
        else: #b==k
            return mj
    if a==j:
        if b==i:
            return mk
        else: # b==k
            return i
    # a==k
    if b==i:
        return j
    else: #b==j
        return mi
    

def stoval(s):
    if s=='i':
        return i
    if s=='j':
        return j
    return k


def main(infilename,outfilename):
    infile = open(infilename,'r')
    outfile = open(outfilename,'w')

    nbr_cases = int(infile.readline().split(' ')[0])
    
    for ctr_cases in range(1,nbr_cases+1):
        line = infile.readline().split(' ')
        pattern_size = int(line[0])
        times = int(line[1])
        pattern = infile.readline()[0:pattern_size];
        res = "NO\n"
        target = i
        last = 1
        for counter in range(times):
            for index in range(pattern_size):
                last = (last&4)^mult(last&3,stoval(pattern[index]))
                if target==last:
                    last = 1
                    if target == j:
                        target = 8
                    if target == i:
                        target = j

        if last == k and target == 8:
            res = "YES\n"

        outline = "Case #" + str(ctr_cases) + ": " + res
        outfile.write(outline)
    infile.close()
    outfile.close()

