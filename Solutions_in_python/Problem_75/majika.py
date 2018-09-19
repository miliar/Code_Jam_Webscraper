import sys


def parset(text):
    lines = [i.strip() for i in text.split("\n") if i.strip()]
    num = int(lines.pop(0))
    test_cases = []
    for line in lines:
        items = line.split()
        num_subs = int(items.pop(0))
        subs = {}
        for i in xrange(num_subs):
            sub = items.pop(0)
            mat = sub[:-1]
            res = sub[-1]
            subs[mat] = res
            subs[mat[::-1]] = res
        
        num_ex = int(items.pop(0))
        exs = {}
        for i in xrange(num_ex):
            ex = items.pop(0)
            exs[ex[0]] = ex[1]
            exs[ex[1]] = ex[0]
        
        items.pop(0)
        elements = items.pop(0)
        test_cases.append({"elems":elements, "exs": exs, "subs": subs})
    return test_cases    

def get_time(case):
    new_string = []
    orig_string = list(case["elems"])
    while True:
        if len(new_string) == 0:
            if not orig_string:
                break
            new_string.append(orig_string.pop(0))
            continue
        if len(new_string) >= 2 and new_string[-2] + new_string[-1] in case["subs"]:
            sub_test = new_string.pop(-2) + new_string.pop(-1)
            new_string.append(case["subs"][sub_test])
            continue
        if new_string[-1] in case["exs"] and case["exs"][new_string[-1]] in new_string:
            new_string = []
            continue
        if not orig_string:
            break
        new_string.append(orig_string.pop(0))
    return "[" + ", ".join(new_string) + "]"

def get_times(parsed):
    for ind, case in enumerate(parsed):
        print "Case #%s: %s" % (ind+1, get_time(case))


if __name__ == '__main__':
   get_times(parset(open(sys.argv[1]).read()))