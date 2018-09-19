def average(l):
    return float(sum(l)) / len(l)

def read_data(f):
    s = file(f).read().splitlines()[1:]
    i = 0
    groups = []
    while i < len(s):
	groups.append(s[i+1:i+1+int(s[i])])
	i = int(s[i])+i+1
    return groups

def compute_wins(group):
    return [(group[i].count('1'), group[i].count('1') + group[i].count('0'))\
                                          for i in xrange(len(group))]
def compute_wp(wins_l):
    return [float(x[0])/x[1] for x in wins_l]

def compute_owp(group,wins_l):
    res = []
    for i,x in enumerate(group):
        res.append(average([(wins_l[j][0] - [1,0][x[j] == '1'])/ float(wins_l[j][1] - 1) for j in xrange(len(x))\
                             if x[j] != '.']))
    return res

    
def compute_rpi(group):
    wins_l = compute_wins(group)
    wp = compute_wp(wins_l)
    owp = compute_owp(group,wins_l)
    oowp = [average([owp[j] for j in xrange(len(group[i])) if group[i][j] != '.']) for i in xrange(len(group))]
    return [0.25 *wp[i] + 0.5 * owp[i] + 0.25 * oowp[i] for i in xrange(len(group))]


def solve_all(inp,out):
    data = read_data(inp)
    res = map(compute_rpi, data)
    f = file(out,"w")
    for i,r in enumerate(res):
        f.write("Case #%d:\n"%(i+1))
        for x in r:
            f.write("%8f\n"%(x,))
    f.close()
