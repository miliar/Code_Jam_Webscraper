import sys
import logging

logging.basicConfig()
log = logging.getLogger(__name__)
#log.setLevel(logging.DEBUG)
log.setLevel(logging.INFO)

def train_timetable(schedule, t):
    log.debug(schedule)
    
    trains = []
    while schedule:
        train = []
        next_time = 0
        direction = ''
        to_remove = []
        for trip in schedule:
            if next_time <= trip[0] and direction != trip[2]:
                next_time = trip[1] + t
                direction = trip[2]
                train.append(trip)
                log.debug(train)
                to_remove.append(trip)
        
        for trip in to_remove:
            schedule.remove(trip)
        trains.append(train)
        
    log.debug(trains)
    
    count_a = 0
    count_b = 0
    for train in trains:
        if train[0][2] == 'a':
            count_a += 1
        else:
            count_b += 1
            
    return [count_a, count_b]

def to_minutes(x2y):
    m2n = []
    
    bhm = x2y[0].split(':')
    bm = int(bhm[0])*60 + int(bhm[1])
    
    ehm = x2y[1].split(':')
    em = int(ehm[0])*60 + int(ehm[1])
    
    m2n.append(bm)
    m2n.append(em)
    
    return m2n



# open files
input = open(sys.argv[1], 'r')
output = open('train_timetable.out', 'w')

# read input
lines = input.readlines()

# N - number of cases
N = int(lines[0])
del lines[0]

for case in range(N):
    
    T = int(lines[0])
    del lines[0]
    
    nanb = lines[0].split(' ')
    NA = int(nanb[0])
    NB = int(nanb[1])
    del lines[0]
    
    schedule = []
    
    for a in range(NA):
        a2b = lines[0].split(' ')
        a2b = to_minutes(a2b)
        a2b.append('a')
        schedule.append(a2b)
        del lines[0]
    
    for b in range(NB):
        b2a = lines[0].split(' ')
        b2a = to_minutes(b2a)
        b2a.append('b')
        schedule.append(b2a)
        del lines[0]
    
    schedule.sort() # todo comparator
    #log.info('Case #' + str(case+1) + ': ' + str(train_timetable(schedule, T)) + '\n')
    res = train_timetable(schedule, T)
    output.write('Case #' + str(case+1) + ': ' + str(res[0]) + ' ' + str(res[1]) + '\n')

input.close()
output.close()
