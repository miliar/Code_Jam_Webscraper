from heapq import *
import itertools

# priority queue from python docs example
# https://docs.python.org/2/library/heapq.html

pq = []                         # list of entries arranged in a heap
entry_finder = {}               # mapping of tasks to entries
REMOVED = '<removed-task>'      # placeholder for a removed task
counter = itertools.count()     # unique sequence count


def add_task(task, priority):
    'Add a new task or update the priority of an existing task'
    if task in entry_finder:
        remove_task(task)
    count = next(counter)
    entry = [priority, count, task]
    entry_finder[task] = entry
    heappush(pq, entry)


def remove_task(task):
    'Mark an existing task as REMOVED.  Raise KeyError if not found.'
    entry = entry_finder.pop(task)
    entry[-1] = REMOVED


def pop_task():
    'Remove and return the lowest priority task. Raise KeyError if empty.'
    while pq:
        priority, count, task = heappop(pq)
        if task is not REMOVED:
            del entry_finder[task]
            return (task, priority)  # change vs docs
    raise KeyError('pop from an empty priority queue')

# end PQ from python docs

OCCUPIED = []


def update_free(index):
    'Afred add an occupied, update all stalls, which status was changed'

    # at the right side
    ls = 0
    stall = OCCUPIED[index] + 1
    while stall != OCCUPIED[index + 1]:
        rs = OCCUPIED[index + 1] - stall - 1
        add_task(stall, (-1 * min(ls, rs), -1 * max(ls, rs), stall))
        ls += 1
        stall += 1

    # at the left side
    rs = 0
    stall = OCCUPIED[index] - 1
    while stall != OCCUPIED[index - 1]:
        ls = stall - OCCUPIED[index - 1] - 1
        add_task(stall, (-1 * min(ls, rs), -1 * max(ls, rs), stall))
        rs += 1
        stall -= 1


with open("C-small-1-attempt0.in") as f:
    TESTS = int(f.readline())
    for test in range(TESTS):
        pq = []
        entry_finder = {}
        counter = itertools.count()

        N, K = tuple(map(int, f.readline().strip().split(" ")))

        OCCUPIED = [-1, 0, N + 1]

        update_free(1)

        st = -1
        pr = ()

        for i in range(K):
            st, pr = pop_task()
            OCCUPIED.append(st)
            OCCUPIED.sort()

            update_free(OCCUPIED.index(st))

        print("Case #{0}: {1} {2}".format(test + 1, -1 * pr[1], -1 * pr[0]))
