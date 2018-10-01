# Usage : run the python interpreter. Then type :
#         import problemA
#         problemA.main("path1", "path2")
#
# path1 is the path to the input file, path2 is the path to the output file
# open the output file and enjoy the result

def main(infilename,outfilename):
    infile = open(infilename,'r')
    outfile = open(outfilename,'w')

    nbr_cases = int(infile.readline().split(' ')[0])
    

    for i in range(1,nbr_cases+1):
        t = infile.readline()
        guests = process_line(t)
        outline = "Case #" + str(i) + ": " + str(guests) + "\n"
        outfile.write(outline)
    


def process_line(line):
    splitted = line.split(' ')
    Smax = int(splitted[0])
    S = splitted[1]
    
    nbr_guests = 0
    counter = int(S[0])
    
    for i in range(1,Smax+1):
        Si = int(S[i])
        diff = i - counter
        if diff > 0:
            nbr_guests += diff
            counter += diff
        counter += Si
    
    return nbr_guests
        
