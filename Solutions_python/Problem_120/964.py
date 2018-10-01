def parse(name):
    in_file = open('%s.in' % name, 'r')
    cases = int(in_file.readline())
    lines = []
    for case in range(cases):
        line = in_file.readline()
        r, t = line.split(' ')
        lines.append('Case #%s: %s\n' % (case + 1, run(int(r), int(t))))
    print ''.join(lines)
    in_file.close()
    out_file = open('%s.out' % name, 'w')
    out_file.writelines(lines)
    out_file.close()

def run(radius, paint):
    rings = 0
    while True:
        paint -= 2 * radius + 1
        radius += 2
        if paint >= 0:
            rings += 1
        else:
            break
    return rings

parse('A-small')
