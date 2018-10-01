## Google Code Jam ##
## Qualification Round ##
## Problem A. Magic Trick ##


def run_case(lines):
    row1 = int(lines[0].strip())
    row2 = int(lines[5].strip())
    
    row1_vals = [int(i) for i in lines[row1].strip().split(' ')]
    row2_vals = [int(i) for i in lines[row2+5].strip().split(' ')]
    
    vals = set(row1_vals).intersection( set(row2_vals) )
    if ( len(vals) == 1 ):
        return str(list(vals)[0])
    if ( len(vals) > 1 ):
        return "Bad magician!"
    if ( len(vals) == 0 ):
        return "Volunteer cheated!"

    print "FAILED"
    assert(False)

f = file('in_small.txt','r')

lines = f.readlines()

cases = int(lines[0].strip())
print "Number of cases", cases

case_len = 10
start = 1
end = start+case_len

out = file('out_small.txt','w')

for case in xrange(0,cases):
    output = run_case(lines[start:end])
    start = end
    end = end+case_len
    out.write("Case #" + str(case+1) + ": " + output + "\n")

f.close()
out.close()

