from bisect import bisect_left, bisect_right

# the algebra required to get to this was actually
# quite fun, in my opinion
def gen_fr(d, l=[], s=0, even=False):
    diff = d - len(l)
    if diff == 0:
        return [l]
    results = []
    for i in range(3):
        if i == 0 and len(l) == 0:
            continue
        j = 2*i*i if even or diff > 1 else i*i
        if s + j < 10:
            results.extend(gen_fr(d,l+[i],s+j,even))
    return results

def build_pal_e(l):
    return int(''.join(map(str,l + l[::-1])))

def build_pal_o(l):
    return int(''.join(map(str,l + l[-2::-1])))

def gen_fine_sq():
    roots = [1,2,3,11,22]
    for i in range(2, 26):
        roots.extend(map(build_pal_o, gen_fr(i, even=False)))
        roots.extend(map(build_pal_e, gen_fr(i, even=True)))
    return sorted(map(lambda x: x**2, roots))

def main():
    name = input(prompt='name')
    lines = open(name+'.in').readlines()
    T = int(lines[0])
    lines = lines[1:]

    s = ''
    fine_sq = gen_fine_sq()
    for c in range(1, T+1):
        result = 'Case #'+str(c)+': '
        A, B = tuple(map(int, lines[0].split(' ')))
        A2 = bisect_left(fine_sq, A)
        B2 = bisect_right(fine_sq, B)
        result += str(B2-A2) + '\n'
        s += result
        del lines[0]
    open(name+'.out', 'w').write(s)

if __name__ == '__main__':
    main()