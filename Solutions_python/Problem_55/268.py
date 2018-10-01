import itertools
import sys


# if you're reading this, realize that I would never use something this ugly in production :S


sys.stdin = open("theme-small1.in")

n_cases = input()
for case in xrange(1, n_cases + 1):

    n_runs, n_seats, n_groups = map(int, raw_input().split())
    _groups = map(int, raw_input().split())

#    if case not in (11, 15, 20, 16, 25, 35, 37, 39, 44):
#       continue
    
    groups = list(_groups)
    enumerated_groups = itertools.cycle(enumerate(groups))
    group_totals = []


    group_n = None
    to_add = 0

    start_groups = {0:0}
    
    group_start, total = enumerated_groups.next()
    while True:
        while True:
#            print [group_n, to_add, total],
            total += to_add
            group_n, to_add = enumerated_groups.next()
            
            if group_n == group_start:
                break
            if total + to_add > n_seats:
                break
        group_totals += [total]

        if len(group_totals) > 10:
            break
        
#        print group_n, to_add

        group_start = group_n
        total = to_add
        to_add = 0
#        group_start, total = enumerated_groups.next()

#        print group_start, #group_totals
        if group_start in start_groups:
            index = start_groups[group_start]
            start_groups, group_totals = group_totals[:index], group_totals[index:]
            break

        start_groups[group_start] = len(group_totals)


    runs_left = n_runs

    profit = sum(start_groups[:runs_left])

    runs_left = max(0, runs_left - len(start_groups))
    
    if runs_left:
        profit += runs_left / len(group_totals) * sum(group_totals)
        profit += sum(group_totals[:runs_left % len(group_totals)])
                        
    print "Case #%d:" % case, profit # % case, n_seats, groups, group_totals, n_runs,
'''

    on_coaster = []

    groups = list(_groups)
    old_profit = profit
    profit = 0
    for run in range(n_runs):
        on_coaster = []
        while True:
            if groups:
                next_group = groups.pop(0)
            else:
                break

            if sum(on_coaster) + next_group > n_seats:
                groups.insert(0, next_group)
                break

            on_coaster.append(next_group)
            
        profit += sum(on_coaster)
        groups += on_coaster

    if profit != old_profit:
        print "Case #%d:" % case, n_seats, _groups, group_totals, n_runs, old_profit, profit
'''
