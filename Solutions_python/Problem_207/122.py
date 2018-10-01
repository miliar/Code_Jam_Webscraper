t = int(raw_input())


def permute(k1, k2, k3, s1, s2, s3, tw=0):
    str = ""
    if k1 > k2 + k3:
        return "F"
    t1 = min(k1, k2)
    str += (s1 + s2) * t1
    k1 -= t1
    k2 -= t1
    if k1 > 0 and k3 > 0:
        t2 = min(k1, k3)
        str += (s1 + s3) * t2
        k1 -= t2
        k3 -= t2
    elif k2 > 0 and k3 > 0:
        t2 = min(k2, k3)
        str += (s3 + s2) * t2
        k2 -= t2
        k3 -= t2
    mov = 0
    if k1 > 0 or k2 > 0:
        return 'F'
    while mov < str.__len__():
        if k3 > 0:
            if mov == 0 and tw == 1 and str[mov] != s3:
                str = str[:mov] + s3 + str[mov:]
                # mov += 1
                k3 -= 1
                mov += 1
                continue
            if str[mov - 1] != s3 and str[mov] != s3:
                str = str[:mov] + s3 + str[mov:]
                # mov += 1
                k3 -= 1
                mov += 1
                continue
        else:
            return str
        mov += 1
    return 'F'


for i in xrange(1, t + 1):
    n, r, o, y, g, b, v = [int(s) for s in raw_input().split(" ")]
    if (o > b and o > 0) or (g > r and g > 0) or (v > y and v > 0):
        print 'Case #{}: {}'.format(i, 'IMPOSSIBLE')
        continue
    if o == b and o > 0:
        if g + r + v +y != 0:
            print 'Case #{}: {}'.format(i, 'IMPOSSIBLE')
        else:
            print 'Case #{}: {}'.format(i, 'OB'*b)
        continue
    if g == r and g > 0:
        if o + b + v +y != 0:
            print 'Case #{}: {}'.format(i, 'IMPOSSIBLE')
        else:
            print 'Case #{}: {}'.format(i, 'GR' * r)
        continue
    if v == y and v > 0:
        if g + r + o + b != 0:
            print 'Case #{}: {}'.format(i, 'IMPOSSIBLE')
        else:
            print 'Case #{}: {}'.format(i, 'VY' * y)
        continue
    b = b - o
    strb = 'OB'*o
    r = r - g
    y = y - v
    str = permute(r, y, b, 'R', 'Y', 'B')
    if str != 'F':
        if o != 0:
            b1 = str.find("B") + 1
            str = str[0:b1] + 'OB'*o + str[b1:]
        if g != 0:
            g1 = str.find("R") + 1
            str = str[0:g1] + 'GR'*g + str[g1:]
        if v != 0:
            v1 = str.find("Y") + 1
            str = str[0:v1] + 'VY'*v + str[v1:]
        print 'Case #{}: {}'.format(i, str)
        continue
    str = permute(b, y, r, 'B', 'Y', 'R')
    if str != 'F':
        if o != 0:
            b1 = str.find("B") + 1
            str = str[0:b1] + 'OB'*o + str[b1:]
        if g != 0:
            g1 = str.find("R") + 1
            str = str[0:g1] + 'GR'*g + str[g1:]
        if v != 0:
            v1 = str.find("Y") + 1
            str = str[0:v1] + 'VY'*v + str[v1:]
        print 'Case #{}: {}'.format(i, str)
        continue
    str = permute(y, b, r, 'Y', 'B', 'R')
    if str != 'F':
        if o != 0:
            b1 = str.find("B") + 1
            str = str[0:b1] + 'OB'*o + str[b1:]
        if g != 0:
            g1 = str.find("R") + 1
            str = str[0:g1] + 'GR'*g + str[g1:]
        if v != 0:
            v1 = str.find("Y") + 1
            str = str[0:v1] + 'VY'*v + str[v1:]
        print 'Case #{}: {}'.format(i, str)
        continue
    str = permute(r, b, y, 'R', 'B', 'Y')
    if str != 'F':
        if o != 0:
            b1 = str.find("B") + 1
            str = str[0:b1] + 'OB'*o + str[b1:]
        if g != 0:
            g1 = str.find("R") + 1
            str = str[0:g1] + 'GR'*g + str[g1:]
        if v != 0:
            v1 = str.find("Y") + 1
            str = str[0:v1] + 'VY'*v + str[v1:]
        print 'Case #{}: {}'.format(i, str)
        continue
    str = permute(b, r, y, 'B', 'R', 'Y')
    if str != 'F':
        if o != 0:
            b1 = str.find("B") + 1
            str = str[0:b1] + 'OB'*o + str[b1:]
        if g != 0:
            g1 = str.find("R") + 1
            str = str[0:g1] + 'GR'*g + str[g1:]
        if v != 0:
            v1 = str.find("Y") + 1
            str = str[0:v1] + 'VY'*v + str[v1:]
        print 'Case #{}: {}'.format(i, str)
        continue
    str = permute(y, r, b, 'Y', 'R', 'B')
    if str != 'F':
        if o != 0:
            b1 = str.find("B") + 1
            str = str[0:b1] + 'OB'*o + str[b1:]
        if g != 0:
            g1 = str.find("R") + 1
            str = str[0:g1] + 'GR'*g + str[g1:]
        if v != 0:
            v1 = str.find("Y") + 1
            str = str[0:v1] + 'VY'*v + str[v1:]
        print 'Case #{}: {}'.format(i, str)
        continue
    print 'Case #{}: {}'.format(i, 'IMPOSSIBLE')



