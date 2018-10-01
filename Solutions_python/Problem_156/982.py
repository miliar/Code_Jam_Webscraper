#!/usr/bin/env python

def main():
    f = open('infinite_house_of_pancakes_input.txt')

    line = f.readline()
    cases = int(line)

    of = open('infinite_house_of_pancakes_output.txt', 'w')
    for i in range(cases):
        res = "Case #%d: %s" % (i+1, test_case(f))
        print(res)
        of.write(res + "\n")
    of.close()
    f.close()


dyn = None

def recursive(plates):
    global dyn
    if plates[0] <= 2:
        return plates[0]

    key = str(plates)
    if key in dyn:
        return dyn[key]

    m = plates[0]
    orig = plates[0]
    l = len(plates)
    plates.append(0)
    for i in range(2, (orig/2)+1):
        plates[0] = i
        plates[l] = orig - i
        m = min(m, 1 + recursive(sorted(plates, reverse = True)))
    return m

def test_case(ff):
    global dyn
    dyn = {}
    D = int(ff.readline().strip())
    plates = [int(n) for n in ff.readline().split()]
    plates.sort(reverse = True)

    return recursive(plates)

main()
