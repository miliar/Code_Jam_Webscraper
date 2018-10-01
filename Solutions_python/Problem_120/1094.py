import sys
import math

def run(func):
    name = sys.argv[1]
    if not name.endswith('.in'):
        name += '.in'
    with open(name) as handle:
        count = int(handle.readline())
        for x in range(count):
            yield func(handle)

def output(data):
    return '\n'.join('Case #%s: %s' % pair for pair in enumerate(data, start=1))

def test(func):
    print output(run(func))

def write(func):
    name = sys.argv[1]
    if name.endswith('.in'):
        name = name[:-2]
    name += 'out'
    with open(name, 'w') as handle:
        handle.write(output(run(func)))

def f(r, t):
    # adjust radius
    r -= 0.5
    # area of unused white circle
    area = r * r
    # total coverable area
    cover = 2.0 * t + area
    # radius of coverable area
    radius = math.sqrt(cover)
    # paint reach radius
    reach = radius - r
    # circles
    circles = int(reach / 2.0)
    return circles

def func(handle):
    return f(*map(int, handle.readline().split(' ')))

test(func)
