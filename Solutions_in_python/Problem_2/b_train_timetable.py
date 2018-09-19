#!/usr/local/bin/python
def sorter(x, y):
    if x['dep'] != y['dep']:
        return cmp(x['dep'],y['dep'])
    else:
        return cmp(x['arr'],y['arr'])
def main():
    for case in range(input()):
        t_around = input()
        a_size, b_size = map(int, raw_input().split())
        schedule = []
        for i in range(a_size + b_size):
            dep, arr = raw_input().split()
            station = 'A' if i < a_size else 'B'
            trip = {}
            trip['dep'] = reduce(lambda x,y: x*60+y, map(int, dep.split(':')))
            trip['arr'] = reduce(lambda x,y: x*60+y, map(int, arr.split(':')))
            trip['start'] = station
            schedule.append(trip)
        schedule.sort(cmp=sorter)
        a = b = 0
        while len(schedule) > 0:
            trip = schedule.pop(0)
            if trip['start'] == 'A':
                a += 1
            else:
                b += 1
            s = [] + schedule
            arr = trip['arr'] + t_around
            start = trip['start']
            n = 0
            for i, v in enumerate(s):
                if v['dep'] >= arr and v['start'] != start:
                    start = schedule[i-n]['start']
                    arr = schedule.pop(i-n)['arr'] + t_around
                    n += 1
        print "Case #%d: %d %d" % (case+1, a, b)
main()
