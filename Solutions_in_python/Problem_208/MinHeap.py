from collections import namedtuple
KVPair = namedtuple('KVPair', ['key', 'value'])

class MinHeap(object):
    def __init__(self):
        self.pairs = []     # list of (item, number)

    def clone(self):
        new = self.__class__()
        new.pairs = list(self.pairs)
        return new

    def _siftDown(self, pos):
        sz = self.size()
        while True:
            left = pos*2+1; right = left+1
            if sz <= left:
                return
            smallerSon = right if (sz > right and self.pairs[right].value < self.pairs[left].value) else left
            if self.pairs[smallerSon].value >= self.pairs[pos].value:
                return
            self._swap(pos, smallerSon)
            pos = smallerSon

    def _siftUp(self, pos):
        while (pos > 0):
            parent = (pos-1)/2
            if self.pairs[parent].value <= self.pairs[pos].value:
                return
            self._swap(pos, parent)
            pos = parent

    def _swap(self, pos1, pos2):
        self.pairs[pos1], self.pairs[pos2] = self.pairs[pos2], self.pairs[pos1]
        self._refreshItemPosition(pos1)
        self._refreshItemPosition(pos2)

    def _validateAdd(self, item, numValue):
        pass

    def _onItemPositionSet(self, item, newPos):
        """newPos<0 if removing item."""
        pass

    def _refreshItemPosition(self, pos):
        self._onItemPositionSet(self.pairs[pos].key, pos)

    def size(self):
        return len(self.pairs)

    def peekMin(self):
        if self.size()==0:
            raise Exception("Empty heap!")
        return self.pairs[0].key

    def minValue(self):
        if self.size()==0:
            raise Exception("Empty heap!")
        return self.pairs[0].value

    def extractMin(self):
        sz = self.size()
        if sz==0:
            raise Exception("Empty heap!")

        prevMin = self.pairs[0].key
        self._onItemPositionSet(prevMin, -1)

        if sz == 1:
            self.pairs[:] = []
        else:        # sz > 1
            self.pairs[0] = self.pairs[sz-1]
            del self.pairs[-1]
            self._refreshItemPosition(0)
            self._siftDown(0)
        return prevMin

    def add(self, item, numValue):
        self._validateAdd(item, numValue)
        last = self.size()
        self.pairs.append(KVPair(key=item, value=numValue))
        self._refreshItemPosition(last)
        self._siftUp(last)


class UpdatableMinHeap(MinHeap):
    def __init__(self):
        super(UpdatableMinHeap, self).__init__()
        self._indexByItem = {}

    def clone(self):
        new = super(UpdatableMinHeap, self).clone()
        new._indexByItem = dict(self._indexByItem)
        return new

    def _validateAdd(self, item, numValue):
        if item in self._indexByItem:
            raise Exception("Item already exists.")

    def _onItemPositionSet(self, item, newPos):
        if newPos < 0:
            del self._indexByItem[item]
        else:
            self._indexByItem[item] = newPos

    def addOrUpdate(self, item, numValue):
        if item in self._indexByItem:
            index = self._indexByItem[item]
            self.pairs[index] = KVPair(key=self.pairs[index].key, value=numValue)
            self._siftUp(index)
            self._siftDown(index)
        else:
            self.add(item, numValue)

    def __contains__(self, item):
        return item in self._indexByItem


class HybridListHeap(object):
    def __init__(self):
        self._heap = MinHeap()
        self._list = []
        self._preparing = True

    def size(self):
        return len(self._list) + self._heap.size()

    def peekMin(self):
        return self._peekOrExtract(False)

    def extractMin(self):
        return self._peekOrExtract(True)

    def _peekOrExtract(self, takeOut):
        if self._preparing:
            self._preparing = False
            self._sortList()

        try:
            heapmin = self._heap.minValue()
        except:
            if not self._list:
                raise  # The heap-empty exception
            uselist = True
        else:
            uselist = self._list and self._list[-1].value <= heapmin

        if uselist:
            listlast = self._list[-1]
            if takeOut:
                del self._list[-1]
            return listlast.key
        else:
            return self._heap.extractMin() if takeOut else self._heap.peekMin()

    def _sortList(self):
        if not self._list:
            return
        cls = self._list[0].value.__class__
        valuecmp = getattr(cls, '__cmp__', None)
        if not valuecmp:
            valuecmp = lambda v1, v2: -1 if v1.__lt__(v2) else 1 if v2.__lt__(v1) else 0
        kvcmp = lambda kv1, kv2: valuecmp(kv1.value, kv2.value)
        self._list.sort(cmp=kvcmp, reverse=True)

    def add(self, item, numValue):
        if self._preparing:
            self._list.append(KVPair(key=item, value=numValue))
        else:
            self._heap.add(item, numValue)

