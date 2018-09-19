
inpath = "A-small-attempt0.in"
outpath = "A-small-attempt0.out"

infile = open(inpath)
outfile = open(outpath, "w")

numcases = int(infile.readline())


def get_mult(probs, backspace_cnt):
    #middle = pow(2, backspace_cnt)
    mult = 1
    for i in range(0, len(probs)-backspace_cnt):
        mult *= (1-probs[i])
    return mult

def backspace_expected(probs, backspace_cnt, B, A):
    mult_left = get_mult(probs, backspace_cnt)
    r_left = (B - A + 1 + 2*backspace_cnt) * mult_left
    r_right = (2*B + 2 - A + 2*backspace_cnt) * (1-mult_left)
    return r_left + r_right

for casenum in range(0, numcases):

    ab = infile.readline().strip().split(" ")
    a = int(ab[0])
    b = int(ab[1])

    probs = [1-float(s) for s in infile.readline().strip().split(" ")]

    print ("Case %d" % (casenum+1))
    #expected = []
    min_expected = b+2
    for backspace_cnt in range(0, a+1):
        expected = backspace_expected(probs, backspace_cnt, b, a)
        if expected<min_expected:
            min_expected = expected

    outfile.write("Case #%d: %f\n" % (casenum+1, min_expected))

print ("DONE")    
infile.close()
outfile.close()

