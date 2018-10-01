import pp
import sys

def do_magic(answer1, cards1, answer2, cards2):
    candidates = cards1[answer1] & cards2[answer2]
    if len(candidates) == 1: return next(iter(candidates))

    return 'Volunteer cheated!' if len(candidates) == 0 else 'Bad magician!'

def read_part(f):
    answer = int(f.readline())
    cards = [set(map(int, f.readline().strip().split())) for i in xrange(4)]

    return (answer - 1, cards)

job_server = pp.Server()

f = open('A-small-attempt0.in', 'r')
T = int(f.readline()) + 1

jobs = []
for test in xrange(1, T):
    answer1, cards1 = read_part(f)
    answer2, cards2 = read_part(f)

    jobs.append(job_server.submit(do_magic, (answer1, cards1, answer2, cards2)))

f.close()

open('output.txt', 'w').write('\n'.join(['Case #%d: %s' % (i + 1, str(job())) for i, job in enumerate(jobs)]))
