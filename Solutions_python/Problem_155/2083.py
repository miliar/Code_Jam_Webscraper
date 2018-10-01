from s.l import examples, test, get


def ce(pf):
    line = get(pf).split(" ")
    return line

if __name__ == "__main__":
    for comb in examples("a", ce):
        (e, example_id) = comb

        max_shyness = int(e.pop(0))
        if max_shyness == 0:
            print "Case #{eid}: {needs}".format(
                needs=0,
                eid=example_id)
        else:
            shyness = map(int, list(e.pop(0)))
            standing = shyness[0]
            needs = 0

            if standing == 0:
                needs += 1

            for i in range(1, max_shyness + 1):
                if not shyness[i] == 0 and standing + needs < i:
                    needs += i - (standing + needs)

                standing += shyness[i]

            print "Case #{eid}: {needs}".format(
                needs=needs,
                eid=example_id)
