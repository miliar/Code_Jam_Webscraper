import sys
from fractions import gcd

def less(l, r):
    return l < r

def compare(l, r):
    if l[0] < r[0]:
        return True

    if l[0] > r[0]:
        return False

    return l[1] < r[1]

class Heap:
    def parent(i):
        return i//2
    def left(i):
        return i*2
    def right(i):
        return i*2+1

    def size(self):
        return len(self.array)-1

    def heapify(self):
        for i in range(self.size()//2+1, 0, -1):
            self.sift_down(i)

    def sift_up(self, i):
        while i > 1:
            pi = Heap.parent(i)

            if self.comp(self.array[i], self.array[pi]):
                tmp = self.array[i]
                self.array[i] = self.array[pi]
                self.array[pi] = tmp

                i = pi
            else:
                break

    def sift_down(self, i):
        while i <= self.size()//2:
            li = Heap.left(i)
            ri = Heap.right(i)
            bi = li

            if ri <= self.size():
                if self.comp(self.array[ri], self.array[li]):
                    bi = ri

            if self.comp(self.array[bi], self.array[i]):
                tmp = self.array[i]
                self.array[i] = self.array[bi]
                self.array[bi] = tmp

                i = bi
            else:
                break

    def push(self, e):
        self.array.append(e)
        self.sift_up(self.size())

    def top(self):
        return self.array[1]

    def pop(self):
        self.array[1] = self.array[-1]

        self.array.pop()

        self.sift_down(1)

    def __init__(self, ar = [], comp = less):
        self.array = [None]
        self.comp = comp
        self.array.extend(ar)

        self.heapify()

def lcm(a, b):
    return (a*b)//gcd(a, b)

def solve(instance):
    N = instance[0]
    M = instance[1]

    s = lcm(M[0], M[1])
    for i in range(2, len(M)):
        s = lcm(s, M[i])

    count = 0
    for i in range(len(M)):
        count += s // M[i]

    #print(count)
    remaining = (N-1) % count
    #print(remaining)

    time = 0

    barbers = []
    for i in range(len(M)):
        barbers.append([time, i])

    Q = Heap(barbers, compare)

    for i in range(remaining):
        barber = Q.top()
        Q.pop()
        time = barber[0]
        which = barber[1]
        #print('Queue '+str(which)+' ETA: '+str(time+M[which]))
        Q.push([time + M[which], which])

    barber = Q.top()
    print(barber[1]+1)

if __name__ == '__main__':
    T = int(sys.stdin.readline().strip())
    IL = []
    for i in range(T):
        line = sys.stdin.readline().strip().split()
        N = int(line[1])
        line = sys.stdin.readline().strip().split()
        line = [int(i) for i in line]

        IL.append((N, line))

    for i in range(T):
        print('Case #'+str(i+1)+': ', end='')
        solve(IL[i])

