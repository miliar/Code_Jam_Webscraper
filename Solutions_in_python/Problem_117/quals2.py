import multiprocessing
import sys
import itertools
import re

class Lawn(object):
    def __init__(self, size, data):
        self.size = size
        self.target = data
        self.maxx = [max(x) for x in data]
        #print [[data[x][y] for x in range(size[0])] for y in range(size[1])]
        self.maxy = [max([data[x][y] for x in range(size[0])]) for y in range(size[1])]
        self.current = [[100 for x in range(size[1])] for y in range(size[0])]


def reader(f):
    return f.readlines()


def writer(f, data):
    f.write(data)


def chunks(l, n, k=0):
    for i in xrange(0, len(l), n):
        yield l[i:i+(n-k)]


def split(data):
    while True:
        if len(data) == 0:
            return
        size = [int(x.strip()) for x in data[0].split(" ")]
        yield Lawn(size, [[int(z.strip()) for z in x.split(" ")] for x in data[1:size[0]+1]])
        data = data[size[0]+1:]


def transform(queue, i, workset):

    for row in range(workset.size[0]):
        for n in range(workset.size[1]):
            if workset.current[row][n] > workset.maxx[row]:
                workset.current[row][n] = workset.maxx[row]

    for column in range(workset.size[1]):
        for n in range(workset.size[0]):
            if workset.current[n][column] > workset.maxy[column]:
                workset.current[n][column] = workset.maxy[column]

    if workset.current == workset.target:
        queue.put("Case #%d: YES" % i)
    else:
        queue.put("Case #%d: NO" % i)
    return

if __name__ == "__main__":
    #read
    data = reader(sys.stdin)

    #extract something
    num_jobs = int(data[0].strip())

    #split
    worksets = [x for x in split(data[1:])]

    if num_jobs != len(worksets):
        sys.stderr.write("Size mismatch: %d, %d\n" % (num_jobs, len(worksets)))
        sys.exit(-1)

    #transform
    queue = multiprocessing.Queue()
    worker = []
    for i, workset in enumerate(worksets):
        p = multiprocessing.Process(name="Worker %d" % i, target=transform, args=(queue, i+1, workset))
        p.start()
        worker.append(p)

    #wait
    for w in worker:
        w.join()

    #accumulate results
    r = []
    for w in worker:
        r.append(queue.get())

    #write
    for x in sorted(r, key=lambda s: int(s[s.find("#")+1:s.find(":")])):
        writer(sys.stdout, x+"\n")
