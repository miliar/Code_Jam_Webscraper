rf = open('B-large.in')
#rf = open('btest')

for i,line in enumerate(rf):
    if i==0: continue
    v = [int(x) for x in line.split(" ")]
    num = v[0]
    num_s = v[1]
    p = v[2]
    scores = v[3:]

    cutoffscore = p*3-2

    cutoffscore_s = p*3-4

    count = sum([1 for x in scores if x>=cutoffscore])
    count_s = min(num_s,sum([1 for x in scores if
        cutoffscore>x>=cutoffscore_s and x>=2]))
    print "Case #%s: %s" % (i,min(num,count+count_s))

