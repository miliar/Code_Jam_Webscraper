
def get_raw():
    choice = int(raw_input()) - 1
    chosen = []
    for i in range(4):
        raw = raw_input()
        if i == choice:
            chosen = set([int(v) for v in raw.split()])
    return chosen


if __name__ == '__main__':
    nb_cases = int(raw_input())
    for case in xrange(nb_cases):
        first_raw = get_raw()
        second_raw = get_raw()
        good_values = first_raw & second_raw
        size = len(good_values)
        result = "Case #%d: " % (case + 1)
        if size == 0:
            result += "Volunteer cheated!"
        elif size == 1:
            result += "%d" % (good_values.pop())
        else:
            result += "Bad magician!"
        print result
