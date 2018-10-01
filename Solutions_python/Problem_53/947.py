class LiveSocket(object):
    def is_on(self):
        return True

class Snapper(object):
    on = False

    def __init__(self, power_source=LiveSocket()):
        self.power_source = power_source
        
    def snap(self):
        if self.power_source.is_on():
            self.on = not self.on

    def is_on(self):
        return self.power_source.is_on() and self.on

class chain(object):
    def __init__(self, length):
        self.snappers = []
        if length:
            self.snappers.append(Snapper(LiveSocket()))
        for _ in range(length - 1):
            self.snappers.append(Snapper(self.snappers[-1]))

    def __getitem__(self, item):
        return self.snappers[item]

    def snap(self):
        for s in reversed(self.snappers):
            s.snap()

def snap_chain(length, snaps):
    c = chain(length)
    for _ in range(snaps):
        c.snap()

    if c[-1].is_on():
        return 'ON'
    return 'OFF'
            
if __name__ == '__main__':
    import sys
    with file(sys.argv[1]) as f:
        lines = f.readlines()[1:]

    for i, line in enumerate(lines):
        print 'Case #%i: %s' % (i + 1, snap_chain(*map(int, line.split())))
