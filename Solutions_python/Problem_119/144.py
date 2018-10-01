inputfile = file("D-small-attempt1.in", "rb")
outputfile = file("D-small-attempt1.out", "wb")
out_s = "Case #%d: %s"
parse_line = lambda: [int(a) for a in inputfile.readline().split()]
v_in = lambda v: "%d_in" % v
v_out = lambda v: "%d_out" % v

class Chest(object):
    def __init__(self, num, req, contains):
        self.req = req
        self.num = num
        self.contains = contains
        self.is_open = False
    def open(self):
        self.is_open = True
    def close(self):
        self.is_open = False
    

def try_solve(opened, unopened, keys):
    global opened_g
    if len(unopened) == 0:
        return True
    if keys == []:
        return False

    # Verify requirements
    all_keys = keys[:]
    for chest in unopened:
        all_keys.extend(chest.contains)
    all_reqs = [chest.req for chest in unopened]
    for c in all_keys:
        if all_keys.count(c) < all_reqs.count(c):
            return False
    for chest in unopened:
        if all_keys.count(chest.req) - chest.contains.count(chest.req) <= 0:
            return False
    
    for chest in unopened:
        if chest.req in keys:
            chest.open()
            keys.remove(chest.req)
            index = unopened.index(chest)
            unopened.remove(chest)
            opened.append(chest)
            keys.extend(chest.contains)
            if try_solve(opened, unopened, keys) == True:
                opened_g.append(chest)
                return True
            for key in chest.contains:
                keys.remove(key)
            keys.append(chest.req)
            opened.remove(chest)
            unopened.insert(index, chest)
            chest.close()
    if len(unopened)==0:
        return True
    return False
            

def solve_single_case():
    global opened_g
    num_keys, num_chests = parse_line()
    my_keys = parse_line()
    my_keys = [a-1 for a in my_keys]
    assert num_keys == len(my_keys)
    chests = []
    for i in xrange(num_chests):
        line = parse_line()
        lock_num, num_keys_inside = line[:2]
        chest_contains = [key_num - 1 for key_num in line[2:]]
        new_chest = Chest(i, lock_num - 1, chest_contains)
        chests.append(new_chest)
        assert len(chest_contains) == num_keys_inside

    
    unopened = chests
    opened = []
    opened_g = []
    if not try_solve(opened, unopened, my_keys):
        return "IMPOSSIBLE"
    return ' '.join(str(a.num+1) for a in opened_g[::-1])

T, = parse_line()
import time
s = time.time()
for ncase in xrange(1,T+1):
    sol = solve_single_case()
    print >>outputfile, out_s % (ncase, sol)
print "Time:", time.time()-s
