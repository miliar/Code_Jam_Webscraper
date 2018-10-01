
def process_game():
    first_line = int(raw_input())
    s1 = []
    s1.append(raw_input().split())
    s1.append(raw_input().split())
    s1.append(raw_input().split())
    s1.append(raw_input().split())
    second_line = int(raw_input())
    s2 = []
    s2.append(raw_input().split())
    s2.append(raw_input().split())
    s2.append(raw_input().split())
    s2.append(raw_input().split())
    res = set(s1[first_line - 1]) & set(s2[second_line - 1])
    if len(res) == 0:
        print "Volunteer cheated!"
    elif len(res) > 1:
        print "Bad magician!"
    else:
        print tuple(res)[0]

for i in xrange(1, int(raw_input()) + 1):
    print "Case #%d:" % (i),
    process_game()
