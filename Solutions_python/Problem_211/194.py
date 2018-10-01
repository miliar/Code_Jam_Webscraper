import functools
import operator

def solve(k, u, Ps):
    Ps.sort()
    Ps = Ps[-k:]
    while u > 1e-6:
        #print((u, Ps))
        n_cores_to_help = 1
        for i in range(1, len(Ps)):
            if Ps[i] == Ps[0]:
                n_cores_to_help += 1
            elif Ps[i] > Ps[0]:
                break
            else:
                raise Exception(Ps)

        target = 1.
        if n_cores_to_help < len(Ps):
            target = min(target, Ps[n_cores_to_help])

        achievement = Ps[0] + u / n_cores_to_help
        target = min(target, achievement)
        spend = n_cores_to_help * (target - Ps[0])
        u -= spend
        for i in range(n_cores_to_help):
            Ps[i] = target

    return functools.reduce(operator.mul, Ps, 1.0)

if __name__ == '__main__':
    import io
    lines = list(io.open('C-small-1-attempt0.in', 'r').readlines())
    i = 1
    x = 1
    while i < len(lines):
        n, k = map(int, lines[i].split())
        u = float(lines[i+1])
        Ps = list(map(float, lines[i+2].split()))
        assert len(Ps) == n
        print('Case #{}: {:.10f}'.format(x, solve(k, u, Ps)))
        i += 3
        x += 1
