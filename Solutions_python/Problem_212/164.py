import sys

def bprint(*things):
    #if case not in (,): return
    #return  # Disable `bprint` function
    for thing in things:
        print >> sys.stderr, thing,
    print >> sys.stderr, ""


def read_input():
    n_people, pack = map(int, raw_input().split())
    people = map(int, raw_input().split())
    return n_people, people, pack

def calculate(input_args):
    n_people, people, pack = input_args
    remains = {0:0, 1:0, 2:0, 3:0}
    for p in people:
        remains[p % pack] += 1
    bprint(case, remains)

    if pack == 2:
        ans = remains[0]
        ans += (remains[1] / 2)
        remains[1] %= 2
        ans += remains[1]

    elif pack == 3:
        ans = remains[0]

        tmp = min(remains[1], remains[2])
        ans += tmp
        remains[1] -= tmp
        remains[2] -= tmp

        if remains[1]:
            ans += (remains[1] + 2) / 3
        if remains[2]:
            ans += (remains[2] + 2) / 3

        if remains[1] and remains[2]:
            bprint("ERROR!!")

    elif pack == 4:
        ans = remains[0]
        # 1, 3
        tmp = min(remains[1], remains[3])
        ans += tmp
        remains[1] -= tmp
        remains[3] -= tmp
        # 2
        tmp = (remains[2] / 2)
        ans += tmp
        remains[2] %= 2
        # fault
        if remains[1] and remains[3]:
            bprint("ERROR!!!!")
        # remains 2(1)
        if (not remains[1]) and (not remains[3]) and remains[2]:
            ans += 1
        # remains 1, 2(1)
        elif remains[1]:
            if remains[2]:
                if remains[1] <= 2:
                    return (ans + 1)
                else:
                    ans += 1
                    remains[1] -= 2
            ans += (remains[1] + 3) / 4
        # remains 3, 2(1)
        elif remains[3]:
            if remains[2]:
                if remains[3] <= 2:
                    return (ans + 1)
                else:
                    ans += 1
                    remains[3] -= 2
            ans += (remains[3] + 3) / 4

    return ans

def to_formated_string(tokens):
    ans = tokens
    return ans

if __name__ == '__main__':
    T = int(raw_input())
    for case in xrange(1, T + 1):
        input_args = read_input()
        result = calculate(input_args)
        answer = to_formated_string(result)
        print 'Case #%d:' % case, answer

