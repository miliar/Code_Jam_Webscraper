import heapq


class PrioritySet(object):
    def __init__(self):
        self.heap = []
        self.set = set()

    def add(self, d):
        if d not in self.set:
            heapq.heappush(self.heap, -d)
            self.set.add(d)

    def get(self):
        d = -heapq.heappop(self.heap)
        self.set.remove(d)
        return d


class BathroomStalls2:
    @staticmethod
    def solve(n, k):
        heap_q = PrioritySet()
        heap_q.add(n)
        dict_q = {n: 1}

        target = None
        while heap_q.heap:
            # print(size_q)
            target = heap_q.get()
            count = dict_q[target]
            k -= count
            # print(k)
            if k <= 0:
                break
            del dict_q[target]

            if target == 1:
                continue
            if target == 2:
                if 1 not in dict_q:
                    dict_q[1] = 0
                dict_q[1] += count
                heap_q.add(1)
                continue

            target -= 1
            x = int(target / 2)
            if target % 2 == 1:
                if x + 1 not in dict_q:
                    dict_q[x + 1] = 0
                if x not in dict_q:
                    dict_q[x] = 0
                dict_q[x + 1] += count
                dict_q[x] += count
                heap_q.add(x + 1)
                heap_q.add(x)
            else:
                if x not in dict_q:
                    dict_q[x] = 0
                dict_q[x] += count * 2
                heap_q.add(x)

        target -= 1
        x = int(target / 2)
        if target % 2 == 1:
            return x + 1, x
        else:
            return x, x

    @staticmethod
    def one_solving(n, k):
        size_q = [n]
        for _ in range(0, k - 1):
            # print(size_q)
            target = size_q.pop(0)
            if target == 1:
                continue
            if target == 2:
                size_q.append(1)
                continue

            target -= 1
            x = int(target / 2)
            if target % 2 == 1:
                size_q.append(x + 1)
                size_q.append(x)
            else:
                size_q.append(x)
                size_q.append(x)
        target = size_q.pop(0)
        target -= 1
        x = int(target / 2)
        if target % 2 == 1:
            return x + 1, x
        else:
            return x, x

    @staticmethod
    def main():
        t = int(input())
        for i in range(0, t):
            s = input()
            n, k = s.split(' ')
            print('Case #%s: %s' % (i + 1, '%s %s' % BathroomStalls2.solve(int(n), int(k))))


if __name__ == "__main__":
    BathroomStalls2.main()
