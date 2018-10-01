
import os

# just to make sure I read the file from the correct directory
if len(os.path.dirname(__file__)) > 0:
    os.chdir(os.path.dirname(__file__))


in_file = r"C-large.in"
out_file = r"out.txt"

def write_test_case(outf, testn, res):
    s = "Case #%d: %s\n" % (testn,res)
    outf.write(s)

with open(out_file, "w") as outf:
    with open(in_file) as f:
        # The first line of the input gives the number of test cases, T.
        T = int(f.readline().strip())
        for i in xrange(0,T):
            print "working on case ", i
            f.readline()    # skip the length line
            line = f.readline()
            c = [int(x) for x in line.strip().split(" ")]
            res = "NO"
            if reduce(lambda a,b :a^b, c)  == 0:
                res = str(sum(c) - min(c))
            write_test_case(outf,i+1,res)
            