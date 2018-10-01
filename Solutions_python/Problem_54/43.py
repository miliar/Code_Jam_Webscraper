import sys

class Reader:
    def __init__(self, filename):
        self.fp = open(filename)
    
    def readline(self):
        return [int(x) for x in self.fp.readline().split()]

def gcd(a, b):
    if a > b:
        return gcd(b, a)
    elif a == b:
        return a
    elif a == 0:
        return b
    else:
        return gcd(b % a, a)

def gcd_list(l):
    assert l
    result = l[0]
    for x in l[1:]:
        result = gcd(result, x)
    return result

if __name__ == '__main__':
    reader = Reader(sys.argv[1])
    cases, = reader.readline()
    for case in range(cases):
        case_data = reader.readline()
        event_count = case_data[0]
        events = case_data[1:]
        assert event_count == len(events)
        first_event = events[0]
        other_events = events[1:]
        diffs = [x - first_event for x in other_events]
        # normalize
        diffs = [abs(x) for x in diffs if x != 0]
        period = gcd_list(diffs)
        periods_since_first_event = first_event / period
        if first_event % period == 0:
            result = 0
        else:
            result = period - first_event % period

        print "Case #%d: %s" % (case + 1, result)
