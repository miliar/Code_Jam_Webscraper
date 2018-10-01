
def mul(x, y):
    x0, x1 = x
    y0, y1 = y
    s, c = x0 * y0, '1'
    if x1 == '1':
        c = y1
    elif y1 == '1':
        c = x1
    elif x1 == y1:
        s *= -1
        c = '1'
    elif x1 == 'i' and y1 == 'j':
        c = 'k'
    elif x1 == 'i' and y1 == 'k':
        s *= -1
        c = 'j'
    elif x1 == 'j' and y1 == 'k':
        c = 'i'
    elif x1 == 'j' and y1 == 'i':
        s *= -1
        c = 'k'
    elif x1 == 'k' and y1 == 'i':
        c = 'j'
    elif x1 == 'k' and y1 == 'j':
        s *= -1
        c = 'i'
    return s, c

def main():
    for t in range(int(input())):
        L, X = map(int, input().split())
        s = str(input())

        val = (1, '1')
        for c in s * (X % 4):
            val = mul(val, (1, c))

        result = True if val == (-1, '1') else False

        if result:
            s = s * (X % 4 + (4 if X >= 4 else 0))
            p1 = p2 = -1

            n1 = (1, '1')
            for i in range(len(s)):
                n1 = mul(n1, (1, s[i]))
                if n1 == (1, 'i'):
                    p1 = i
                    break

            n2 = (1, '1')
            for i in range(len(s)-1, -1, -1):
                n2 = mul((1, s[i]), n2)
                if n2 == (1, 'k'):
                    p2 = i
                    break

            result = (p1 > -1 and p2 > -1) and p1 < p2 + (X * L - len(s))

        print('Case #%d:' % (t + 1), ('YES' if result else 'NO'))

if __name__ == "__main__":
    main()
