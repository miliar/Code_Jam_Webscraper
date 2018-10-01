infile = open("C-large.in")
outfile = open("C-large.out",'w')
lines = infile.readlines()
cases = int(lines[0])
del lines[0]
offset = 0
def add(x,y): return x+y
for case in range(1, cases+1):
    possible = True
    num_candy = int(lines[0])
    del lines[0]
    values = map(int,lines[0].split())
    del lines[0]
    total = 0
    sean = 0
    patrick = 0
    for val in values:
        total = total^val
    if total == 0:
        values.sort()
        del values[0]
        sean = reduce(add,values)
        
        outfile.write( "Case #%d: %d\n" % (case,sean))
    else:
        outfile.write( "Case #%d: NO\n" % case)

infile.close()
outfile.close()
