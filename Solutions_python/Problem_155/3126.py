__author__ = 'mdaley'


def read_input(filename):
    with open(filename, 'rb') as f:

        t = int(f.readline())
        cases = []
        for _ in range(t):
            line = f.readline()
            s_max = int(line.split()[0])
            audience = [int(x) for x in line.split()[1]]
            cases.append((s_max, audience))

        return cases


def invite_friends(audience):

    running_count = 0
    friends_needed = 0
    for shyness_level, level_count in enumerate(audience):

        if level_count == 0:
            continue

        elif running_count >= shyness_level:
            # people on this level will applaud
            running_count += level_count

        else:
            # need some help
            to_invite = shyness_level - running_count
            running_count += to_invite + level_count
            friends_needed += to_invite

    return friends_needed


def test(filename):
    cases = read_input(filename)
    for i, case in enumerate(cases):
        print 'Case #{case_num}: {friend_count}'.format(case_num=i+1, friend_count=invite_friends(case[1]))