# pp@myelin.co.nz
# magicka
# google code jam qual B

NOISY = 0

T = int(raw_input())
for case in range(T):
    line = raw_input().strip().split()
    if NOISY: print "\n===", line

    # read combinations
    combos = {}
    C = int(line.pop(0))
    for c in range(C):
        a, b, result = line.pop(0)
        combos["".join(sorted([a, b]))] = result
    if NOISY: print "combos:", combos

    # read opposed pairs
    opposed = {}
    D = int(line.pop(0))
    for d in range(D):
        a, b = line.pop(0)
        opposed.setdefault(a, []).append(b)
        opposed.setdefault(b, []).append(a)
    if NOISY: print "opposed:", opposed

    # read actual string
    N = int(line.pop(0))
    str, = line
    assert len(str) == N

    if NOISY: print combos, opposed, str

    elements = []

    for el in str:
        elements.append(el)

        # check the last two elements for a combination
        if len(elements) >= 2:
            possible_combo = "".join(sorted(elements[-2:]))
            if NOISY: print "check for combo: %s" % possible_combo
            if combos.has_key(possible_combo):
                if NOISY: print "   combo found:",elements
                elements.pop()
                elements.pop()
                elements.append(combos[possible_combo])
                if NOISY: print "        now ",elements
            else:
                if NOISY: print "no combo found; check for opposition"
                for op in opposed.get(el, []):
                    if NOISY: print "  check %s" % op
                    if op in elements:
                        if NOISY: print "    opposition!  clear list"
                        elements = []

        # index the current element list so we can check for opposed elements quickly
        seen = {}
        for e in elements: seen[e] = 1

    print "Case #%d: [%s]" % (case+1, ", ".join(elements))
