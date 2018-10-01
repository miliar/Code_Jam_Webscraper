import sys

def parse_time(s):
    return (int(s[0:2])*60+int(s[3:5]), int(s[6:8])*60+int(s[9:11]))

# read the whole file specified as an argument into memory
filename = "train_timetable.in"
if len(sys.argv) > 1:
    filename = sys.argv[1]
lines = [line.strip() for line in open(filename)]

# process the cases
cases = int(lines[0])
offset = 1
for case in range(1, cases + 1):

    # extract the timetable details - convert times to mins after midnight
    t = int(lines[offset])
    na = int(lines[offset + 1].split(" ")[0])
    nb = int(lines[offset + 1].split(" ")[1])
    a_to_bs = [parse_time(lines[i]) for i in range(offset + 2, offset + 2 + na)]
    b_to_as = [parse_time(lines[i]) for i in range(offset + 2 + na, offset + 2 + na + nb)]
    offset = offset + 2 + na + nb

    # simulate by ticking a clock from midnight
    a_to_bs.sort()
    b_to_as.sort()
    fa, fb, ma, mb = 0, 0, 0, 0
    for time in range(0, 24*60):

        # free up any arrived trains at b
        for a_to_b in a_to_bs:
            if (a_to_b[1] + t) == time:
                fb = fb + 1

        # free up any arrived trains at a
        for b_to_a in b_to_as:
            if (b_to_a[1] + t) == time:
                fa = fa + 1


        # depart trains from a
        for a_to_b in a_to_bs:
            if (a_to_b[0]) == time:
                fa = fa - 1
                ma = min(fa, ma)

        # depart trains from b
        for b_to_a in b_to_as:
            if (b_to_a[0]) == time:
                fb = fb - 1
                mb = min(fb, mb)

    # output the results
    print "Case #%d: %d %d" % (case, abs(ma), abs(mb))
#    print "Case #%d: t=%d na=%d nb=%d a_to_bs=%s b_to_as=%s" % (case, t, na, nb, a_to_bs, b_to_as)
