__author__ = 'ivandasch'
import sys

default_rate = 2.0

def memoize(f):
    """ Memoization decorator for functions taking one or more arguments. """
    class memodict(dict):
        def __init__(self, f):
            self.f = f
        def __call__(self, *args):
            return self[args]
        def __missing__(self, key):
            ret = self[key] = self.f(*key)
            return ret
    return memodict(f)

@memoize
def time_to_build_factories(n, farm_cost, farm_rate):
    ret = 0.0
    for i in xrange(0,n):
        ret += farm_cost/(i*farm_rate + default_rate)
    return ret



def task_solver(farm_cost,farm_rate,goal):
    ret = goal/default_rate
    i = 0
    while True:
        i += 1
        new_time = time_to_build_factories(i,farm_cost,farm_rate) + goal/(i*farm_rate + default_rate)
        if new_time > ret:
            break
        else:
            ret = new_time
    return round(ret,7)

with open(sys.argv[1]) as file:
    num_tasks = int(file.readline())
    for i in range(0,num_tasks):
        data = [float(j) for j in file.readline().split()]
        print 'case #%s: %s' % (str(i+1), str(task_solver(*data)))


