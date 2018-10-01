import argparse
import copy
import sys

class Runner(object):
    class State(object):
        def __init__(self, me, motes):
            self._me = me
            self._motes = [m for m in reversed(sorted(motes))]
            self._operations = 0

        def __repr__(self):
            return str(self)

        def __str__(self):
            return '%s: %s {%s}' % (self._me, str(self._motes), self._operations,)

        def consume(self):
            while len(self._motes) != 0:
                m = self._motes[-1]
                if m < self._me:
                    self._me += m
                    self._motes.pop()
                else:
                    break
            return len(self._motes) == 0

        def add(self):
            flag = True

            v = self._me - 1
            if v <= 0:
                flag = False
            else:
                self._motes.append(v)
                self._operations += 1

            return flag

        def remove(self):
            self._motes.pop(0)
            self._operations += 1
            return True

        @property
        def operations(self):
            return self._operations

    def __init__(self, me, motes):
        self._initial = Runner.State(me, motes)

    def solve(self):
        results = self.solve0(self._initial)
        return min([r.operations for r in results])

    def solve0(self, state):
        results = []

        is_done = state.consume()
        if not is_done:
            state1 = copy.deepcopy(state)
            if state1.add():
                results.extend(self.solve0(state1))
            state2 = copy.deepcopy(state)
            if state2.remove():
                results.extend(self.solve0(state2))
        else:
            results.append(state)

        return results

def main(args=sys.argv[1:]):
    parser = argparse.ArgumentParser()
    parser.add_argument('file', nargs=1)
    arguments = parser.parse_args(args)

    with open(arguments.file[0], 'r') as f:
        n = int(f.readline())
        for i in range(0, n):
            mote, n_motes = f.readline().strip().split(' ')
            motes = f.readline().strip().split(' ')
            assert len(motes) == int(n_motes)

            runner = Runner(int(mote), [int(m) for m in motes])
            print 'Case #%d: %s' % (i+1, runner.solve(),)

if __name__ == '__main__':
    sys.exit(main())
