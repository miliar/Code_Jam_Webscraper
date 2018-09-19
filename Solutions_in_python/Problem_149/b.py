from multiprocessing import Pool
import itertools

def read_array(convertor=None):
    ret = raw_input().split()
    if convertor: ret = map(convertor, ret)
    return ret

#======================== BOF  =============================#

def dist(a, A):
    A = A[:]
    m = {}
    for i, x in enumerate(a):
        m[x] = i

    for i in range(len(A)):
        A[i] = m[A[i]]

    return cal(A)


def cal(a):
    ans = 0
    l = len(a)
    for i in range(l):
        j = i
        while j > 0 and a[j] < a[j-1]:
            a[j-1], a[j] = a[j], a[j-1]
            ans += 1
            j -= 1

    return ans
    

def updown(a):
    l = len(a)
    largest = a[0]
    largest_i = 0
    for i in range(l):
        if a[i] > largest:
            largest = a[i]
            largest_i = i
    j = largest_i
    while j > 0:
        if a[j] < a[j-1]:
            return False
        j -= 1

    j = largest_i
    while j < l - 1:
        if a[j] < a[j+1]:
            return False
        j += 1

    return True

def solver(data_container):
    N = data_container.N
    A = data_container.A

    ans = 10 ** 100
    for a in itertools.permutations(A):
        if updown(a):
            ans = min(ans, dist(a, A))

    return ans


class DataContainer:
    def __init__(self):
        self.N = input()
        self.A = read_array(int)

#======================== EOF  =============================#


if __name__ == '__main__':
    NUM_THREAD = 2
    USE_MULTI = False

    T = input()
    input_queue = [DataContainer() for _ in xrange(T)]
    
    if USE_MULTI:
        pool = Pool(NUM_THREAD)
        result = pool.map(solver, input_queue)
    else:
        result = []
        for i in xrange(T):
            result.append(solver(input_queue[i]))

    for i in range(T):
        print 'Case #%d: %s' % (i+1, result[i])
