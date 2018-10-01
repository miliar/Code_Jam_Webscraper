def int_input():
    return int(raw_input())

def list_int_input():
    l = raw_input().split()
    for i, v in enumerate(l):
        l[i] = int(v)
    return l

def main():
    for c in range(int_input()):
        rounds, seats, groups_len = list_int_input()
        groups = list_int_input()
        income = 0
        for r in range(rounds):
            used_seats = 0
            play_groups = list()
            while used_seats < seats and len(groups) > 0:
                if used_seats + groups[0] > seats:
                    break
                used_seats += groups[0]
                income += groups[0]
                play_groups.append(groups[0])
                del groups[0]
            groups += play_groups
        print 'Case #%d: %d' % (c+1, income)

main()
