import sys
from collections import defaultdict, OrderedDict


def print_solutions(filename):
    content = open(filename).read().strip().split('\n')
    test_case_count = int(content[0])
    i = 1
    while i <= test_case_count:
        slots, people = [int(m) for m in content[i].split(' ')]
        if slots == people:
            mx = 0
            mn = 0
        else:
            data = OrderedDict()
            for s in range(slots):
                l = s
                r = slots - s - 1
                data[s] = {'l': l, 'r': r, 'mn': min(l, r), 'mx': max(l, r)}
            val = None
            for __ in range(people):
                sorted_data = sorted(data.items(), key=lambda (k, v): (-v['mn'], -v['mx']))
                val = sorted_data[0][1]
                chosen_slot = sorted_data[0][0]
                #print(chosen_slot)
                #print(data)
                del data[chosen_slot]
                for key in range(chosen_slot + 1, slots):
                    if key not in data:
                        break

                    r = data[key]['r']
                    l = key - chosen_slot - 1
                    data[key] = {'l': l, 'r': r, 'mn': min(l, r), 'mx': max(l, r)}

                for key in range(chosen_slot - 1, -1, -1):
                    if key not in data:
                        break

                    l = data[key]['l']
                    r = chosen_slot - key - 1
                    data[key] = {'l': l, 'r': r, 'mn': min(l, r), 'mx': max(l, r)}
                #for key in data.keys():
                #    c = False
                #    l = data[key]['l']
                #    r = data[key]['r']
                #    if key < chosen_slot and r >= chosen_slot:
                #        r = chosen_slot - key - 1
                #        c = True
                #    elif key > chosen_slot and l >= slots - chosen_slot - 1:
                #        l = key - chosen_slot - 1
                #        c = True
                #    if c:
                #        data[key] = {'l': l, 'r': r, 'mn': min(l, r), 'mx': max(l, r)}
            #print(data)

            mx = val['mx']
            mn = val['mn']
        print("Case #%s: %s %s" % (i, mx, mn))
        i += 1

filename = sys.argv[1]
print_solutions(filename)
