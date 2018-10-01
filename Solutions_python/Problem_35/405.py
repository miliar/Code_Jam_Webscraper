class Cell(object):
    _left_neighbor = None
    _right_neighbor = None
    _top_neighbor = None
    _bottom_neighbor = None

    def __init__(self, altitude, left_neighbor=None, top_neighbor=None):
        self._dependent_groups = []
        self.altitude = altitude
        if left_neighbor is not None:
            self.left_neighbor = left_neighbor
        if top_neighbor is not None:
            self.top_neighbor = top_neighbor
        self._group = group_ids.next()

    def set_group(self, group):
        self._group = group
        for dep in self._dependent_groups:
            dep.group = group
    group = property(lambda self:self._group, set_group)

    def add_group_dependency(self, cell):
        self._dependent_groups += [cell]

    def set_left_neighbor(self, neighbor, internal_setter=False, is2=False):
        self._left_neighbor = neighbor
        if not internal_setter:
            neighbor.set_right_neighbor(self, True)
    left_neighbor = property(lambda self:self._left_neighbor, set_left_neighbor)

    def set_right_neighbor(self, neighbor, internal_setter=False, is2=False):
        self._right_neighbor = neighbor
        if not internal_setter:
            neighbor.set_left_neighbor(self, True)
    right_neighbor = property(lambda self:self._right_neighbor, set_right_neighbor)

    def set_top_neighbor(self, neighbor, internal_setter=False, is2=False):
        self._top_neighbor = neighbor
        if not internal_setter:
            neighbor.set_bottom_neighbor(self, True)
    top_neighbor = property(lambda self:self._top_neighbor, set_top_neighbor)

    def set_bottom_neighbor(self, neighbor, internal_setter=False, is2=False):
        self._bottom_neighbor = neighbor
        if not internal_setter:
            neighbor.set_top_neighbor(self, True)
    bottom_neighbor = property(lambda self:self._bottom_neighbor, set_bottom_neighbor)

    def all_neighbors(self):
        """ Return all neighbors in this order: north, west, east, south """
        return (self.top_neighbor, self.left_neighbor,
                self.right_neighbor, self.bottom_neighbor)

    def lowest_neighbor(self):
        """ Return the neighbor of the cell with the lowest altitude """
        def _min(x):
            m = None
            for i in x:
                if i is not None:
                    if m is None or i < m:
                        m = i
            return m
        return _min(self.all_neighbors())

    def __cmp__(self, other):
        return cmp(self.altitude, other.altitude)

    def __repr__(self):
        return '<Cell (A=%d)>' % self.altitude

from itertools import count
group_ids = count()

def find_groups(map):
    def _charpool():
        for c in 'abcdefghijklmnopqrstuvwxyz':
            yield c
    charpool = _charpool()
    chars = {}
    def char_for_number(n):
        if n in chars:
            return chars[n]
        else:
            chars[n] = charpool.next()
            return chars[n]

    resmap = []
    max_cell_index = len(map[0])
    for row_index, row in enumerate(map):
        _row = []
        for cell_index, altitude in enumerate(row):
            cell = Cell(altitude)
            _row.append(cell)
            if row_index > 0:
                cell.top_neighbor = resmap[row_index-1][cell_index]
            if 0 < cell_index < max_cell_index:
                cell.left_neighbor = _row[cell_index-1]
        resmap.append(_row)

    for row in resmap:
        for cell in row:
            lowest_neighbor = cell.lowest_neighbor()
            if lowest_neighbor is None:
                # should happen
                continue
            if lowest_neighbor < cell:
                cell.group = lowest_neighbor.group
                lowest_neighbor.add_group_dependency(cell)

    for row in resmap:
        for cell in row:
            print char_for_number(cell.group),
        print '\n',

if __name__ == '__main__':
    with open('B-large.in') as fobj:
        input = fobj.read().split('\n')[:-1]
    testcases = input.pop(0)
    i = 1
    while input:
        number_of_rows = int(input.pop(0).split()[0])
        print "Case #%d:" % i
        _map = map(lambda x:map(int, x.split()), (input.pop(0) for x in range(number_of_rows)))
        find_groups(_map)
        i += 1
