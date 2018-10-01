
def compute_total_cam(passes, starter):
    total_cam = 0
    time = 0
    holder = starter
    for p in passes + [1440]:
        if holder == 'cam':
            holder = 'jam'
            total_cam += p - time
            time = p
        else:
            holder = 'cam'
            time = p
    return total_cam


def compute_intervals(passes, starter):
    holder = starter
    time = 0
    intervals = []
    for p in passes:
        s, e = time, p
        intervals.append((s, e, holder))
        time = p
        if holder == 'jam':
            holder = 'cam'
        else:
            holder = 'jam'
    if time != 1440:
        intervals.append((time, 1440, holder))
    return intervals


def compute_free_intervals(intervals, tasks, whom):
    free_intervals = []
    for s, e, holder in intervals:
        if holder == whom:
            continue

    for (s1, e1), (s2, e2) in zip(tasks[:-1], tasks[1:]):
        for si, ei, hi in intervals:
            if hi == whom:
                continue
            if si <= e1 and s2 <= ei:
                free_intervals.append((e1, s2))
    return free_intervals


def extreme_balance(cam, jam, passes, starter):
    total_cam = compute_total_cam(passes, starter)
    intervals = compute_intervals(passes, starter)
    if total_cam > 720:
        delta = 0
        free_intervals = compute_free_intervals(intervals, jam, 'jam')
        free_intervals.sort(key=lambda (s, e): e - s)
        free_intervals.reverse()
        for iv in free_intervals:
            delta += 2
            total_cam -= iv[1] - iv[0]
            if total_cam <= 720:
                return delta
    elif total_cam < 720:
        delta = 0
        free_intervals = compute_free_intervals(intervals, cam, 'cam')
        free_intervals.sort(key=lambda (s, e): e - s)
        free_intervals.reverse()
        for iv in free_intervals:
            delta += 2
            total_cam += iv[1] - iv[0]
            if total_cam >= 720:
                return delta
    else:
        return 0
    return 100000000


def balance_times(cam, jam, passes, starter):
    total_cam = compute_total_cam(passes, starter)

    newpasses = []
    holder = starter
    time = 0
    if total_cam > 720:
        timerem = total_cam - 720
        for p in passes:
            if holder == 'cam':
                earliest = max([e for s, e in jam if e <= p and e >= time] + [0])
                delta = p - earliest
                if delta > timerem:
                    passtime = p - timerem
                else:
                    passtime = p - delta
                newpasses.append(passtime)
                timerem -= p - passtime
                holder = 'jam'
                time = passtime
            else:
                newpasses.append(p)
                holder = 'cam'
                time = p
    elif total_cam < 720:
        timerem = 720 - total_cam
        for p in passes:
            if holder == 'jam':
                earliest = max([e for s, e in cam if e <= p and e >= time] + [0])
                delta = p - earliest
                if delta > timerem:
                    passtime = p - timerem
                else:
                    passtime = p - delta
                newpasses.append(passtime)
                timerem -= p - passtime
                holder = 'cam'
                time = passtime
            else:
                newpasses.append(p)
                holder = 'jam'
                time = p
    else:
        newpasses = passes
    return newpasses


def minimize_passes(cam, jam, starter='cam'):
    time = 0
    passes = []
    holder = starter
    while time < 1440:
        if holder == 'cam':
            tasks = cam
            nextholder = 'jam'
        else:
            tasks = jam
            nextholder = 'cam'
        future_jobs = [s for s, e in tasks if s >= time]
        if len(future_jobs) > 0:
            nextpass = min(future_jobs)
            passes.append(nextpass)
            holder = nextholder
            time = nextpass
        else:
            # If there are no more jobs for this guy, just let him hold it til the end
            time = 1440

    # Once we hit midnight, the holder has to pass it back to the starter
    if holder != starter:
        passes.append(time)
    return passes

cases = int(raw_input())

for ctr in xrange(cases):
    ss = raw_input().split(" ")
    ccam = int(ss[0])
    cjam = int(ss[1])
    tcam = []
    for x in xrange(ccam):
        ss = raw_input().split(" ")
        s, e = int(ss[0]), int(ss[1])
        tcam.append((s, e))
    tcam.sort()

    tjam = []
    for x in xrange(cjam):
        ss = raw_input().split(" ")
        s, e = int(ss[0]), int(ss[1])
        tjam.append((s, e))
    tjam.sort()

    result = None
    for starter in ['cam', 'jam']:
        passes = minimize_passes(tcam, tjam, starter)
        # print 'minimized', starter, passes
        passes = balance_times(tcam, tjam, passes, starter)
        delta = extreme_balance(tcam, tjam, passes, starter)
        if result is None:
            result = starter, passes, delta
        else:
            s, p, d = result
            if len(p) + d > len(passes) + delta:
                result = starter, passes, delta

    starter, passes, delta = result
    # print compute_total_cam(passes, starter), passes, delta, starter
    print "Case #{}: {}".format(ctr + 1, len(passes) + delta)
