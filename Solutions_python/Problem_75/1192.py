import argparse, collections

def solve(scombos, sbads, squeue):
    combos = {}
    for c in scombos:
        combos[(c[0],c[1])]=c[2]
        combos[(c[1],c[0])]=c[2]
    bads = collections.defaultdict(set)
    for b in sbads:
        bads[b[0]].add(b[1])
        bads[b[1]].add(b[0])

    els = [-1]
    for c in squeue:
        if (els[-1], c) in combos:
            els[-1] = combos[(els[-1], c)]
            continue

        clear = False
        for existing in els:
            if existing in bads[c]:
                clear = True
                break
        if clear:
            els = [-1]
        else:
            els.append(c)
                    
    return els[1:]


def main(args):
    with open(args.file) as f:
        T = int(f.readline())
        n = 1
        for line in f:
            parts = line.split(' ')
            C = int(parts[0])
            Cstrs = parts[1:1+C]
            D = int(parts[1+C])
            Dstrs = parts[2+C:2+C+D]
            queue = parts[-1].rstrip()
            s = solve(Cstrs, Dstrs, queue)
            sstr = '[' + ', '.join(s) + ']'
            print "Case #{!s}: {}".format(n, sstr)
            n += 1


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('file')
    args = parser.parse_args()
    main(args)
