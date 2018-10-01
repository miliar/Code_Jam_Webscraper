from fractions import Fraction

def f():
    d, n = map(int, input().split())
    vk, vs = d, 0
    for k, s in sorted((tuple(map(int, input().split())) for i in range(n)), reverse=True):
        if s <= vs:
            vk, vs = k, s
        else:
            t = Fraction(vk - k, s - vs)
            if s * t + k >= d:
                vk, vs = k, s
    return d * vs / (d - vk)

for t in range(int(input())):
    print('Case #{}: {}'.format(t + 1, f()))
