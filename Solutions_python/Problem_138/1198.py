import sys

def rl():
    return sys.stdin.readline().strip()

def main():
    T = int(rl())
    for i_ in range(1, T+1):
        N = int(rl())
        naomi = sorted(map(float, rl().split()))
        ken = sorted(map(float, rl().split()))
        w = 0
        naomi_war = list(naomi)
        ken_war = list(ken)
        while naomi_war:
            x = naomi_war.pop(0)
            for i, y in enumerate(ken_war):
                if y > x:
                    ken_war.pop(i)
                    break
            else:
                ken_war.pop(0)
                w += 1
        d = 0
        while naomi:
            y = ken.pop(0)
            for i, x in enumerate(naomi):
                if x > y:
                    naomi.pop(i)
                    d += 1
                    break
            else:
                naomi.pop(0)
        print 'Case #%d: %d %d' % (i_, d, w)

if __name__ == '__main__':
    main()
