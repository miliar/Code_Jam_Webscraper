import math
from collections import namedtuple
Activity = namedtuple('Activity', ['start', 'end', 'host'])

def activity_length(activity):
    return (activity.end - activity.start) % (24*60)

def cover(c_activities, j_activities, host):
    all_activities = c_activities + j_activities
    all_activities = sorted(all_activities, key=lambda x: x.start)
    coverable = find_coverable(all_activities, host)
    sorted_coverable = sorted(coverable, key=activity_length)
    rest_time = 12 * 60 - total_time(c_activities)
    cover_times = 0
    #print(sorted_coverable)
    for c in sorted_coverable:
        if activity_length(c) <= rest_time:
            rest_time-=activity_length(c)
            cover_times+=1
        else:
            break
    #print(cover_times)
    return cover_times

def find_coverable(activies, host):
    total_activities = len(activies)
    coverable = []
    for i in range(total_activities):
        if activies[i].host == host and activies[(i+1)%total_activities].host == host:
            coverable.append(
                Activity(
                    activies[i].end,
                    activies[(i+1)%total_activities].start,
                    'coverable'
                )
            )
    return coverable

def total_time(activities):
    return sum([activity_length(a) for a in activities])

def calc(c, j):
    return max(c, j)*2

T = int(input())
for case in range(T):
    A_c, A_j = input().split()
    A_c, A_j = int(A_c), int(A_j)
    c_activities = []
    j_activities = []
    for i in range(A_c):
        s, e = input().split()
        c_activities.append(Activity(int(s), int(e), 'c'))
    for i in range(A_j):
        s, e = input().split()
        j_activities.append(Activity(int(s), int(e), 'j'))

    c_cover_times=cover(c_activities, j_activities, 'c')
    j_cover_times=cover(j_activities, c_activities, 'j')

    #print(A_c, c_cover_times, A_j, j_cover_times)

    print('Case #{0}: {1}'.format(case+1, calc(A_c-c_cover_times, A_j-j_cover_times)))
