import sys

def handle_case(f, case):
    n = int(f.readline().strip())
    naomi = set([float(x) for x in f.readline().split()])
    ken = set([float(x) for x in f.readline().split()])

    w = handle_war(n, naomi.copy(), ken.copy())
    dw = handle_deceitful_war(n, naomi.copy(), ken.copy())
    print "Case #%d: %d %d"%(case + 1, dw, w)


# Ken always plays the next heaviest, unless he can't win,
# when he plays the lightest
def handle_war(n, naomi, ken):
    points = 0
    for i in xrange(n):
        naomi_weight = min(naomi)
        naomi.remove(naomi_weight)
        ken_weight = get_and_remove_block(ken, naomi_weight)
        if naomi_weight > ken_weight:
            points = points + 1
    return points

def handle_deceitful_war(n, naomi, ken):
    points = 0
    for i in xrange(n):

        naomi_weight = min(naomi)
        naomi.remove(naomi_weight)
        if naomi_weight > min(ken):
            told_weight = 1.0
        else:
            told_weight = max(max(ken) - 0.000001, naomi_weight)
        ken_weight = get_and_remove_block(ken, told_weight)
        if naomi_weight > ken_weight:
            points = points + 1
    return points

# Handle Ken's logic
def get_and_remove_block(ken, weight):
    if weight > max(ken):
        ret = min(ken)
        ken.remove(ret)
        return ret

    copy = ken.copy()
    for e in ken:
        if e < weight:
            copy.remove(e)

    ret = min(copy)
    ken.remove(ret)
    return ret





f = open(sys.argv[1])
cases = int(f.readline().strip())

for i in xrange(cases):
    handle_case(f, i)
