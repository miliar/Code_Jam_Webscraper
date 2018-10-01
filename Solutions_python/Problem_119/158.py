#!/usr/bin/python

import sys

def emit(text, *args):
    msg = text % args
    sys.stderr.write(msg)
    sys.stdout.write(msg)

def getline():
    return sys.stdin.readline().rstrip('\n')

def enough_keys(keys, keys_needed, contents):
    keys = dict(keys)
    for c in contents.values():
        for k in c:
            keys[k] = keys.get(k, 0) + 1
    for k in keys.keys():
        if keys[k] < keys_needed.get(k, 0):
            return False
    return True

def solve_inner(keys, keys_needed, locks, contents):
    solution = [] 
    chests = len(locks)
    while len(solution) < chests:
        for i in sorted(locks.keys()):
            have = keys.get(locks[i], 0)
            if have == 0:
                continue  # no key for this chest
            if have > 1 \
               or have >= keys_needed.get(locks[i], 0) \
               or locks[i] in contents[i]:
                # safe to open
                keys[locks[i]] -= 1
                keys_needed[locks[i]] -= 1
                del locks[i]
                for k in contents[i]:
                    keys[k] = keys.get(k, 0) + 1
                solution.append(i + 1)
                break
            # try opening it, see if there is a solution
            keys_dup = dict(keys)
            keys_needed_dup = dict(keys_needed)
            locks_dup = dict(locks)
            keys_dup[locks[i]] -= 1
            keys_needed_dup[locks[i]] -= 1
            del locks_dup[i]
            for k in contents[i]:
                keys_dup[k] = keys_dup.get(k, 0) + 1
            s2 = solve_inner(keys_dup, keys_needed_dup, locks_dup, contents)
            if s2 == "IMPOSSIBLE":
                continue
            return solution + [i+1] + s2
        else:
            return "IMPOSSIBLE"
    return solution

def solve(keys_arr, locks, contents):
    keys = {}
    for k in keys_arr:
        keys[k] = keys.get(k, 0) + 1
    keys_needed = {}
    for k in locks.values():
        keys_needed[k] = keys_needed.get(k, 0) + 1
    if not enough_keys(keys, keys_needed, contents):
        return "IMPOSSIBLE"
    s = solve_inner(dict(keys), dict(keys_needed), dict(locks), contents)
    if s == "IMPOSSIBLE":
        return s
    # verify solution
    for c in s:
        c = c - 1
        if c not in locks:
            emit("ERROR double open of %d\n", c)
            break
        if keys.get(locks[c], 0) <= 0:
            emit("ERROR no key for %d\n", c)
            break
        keys[locks[c]] = keys[locks[c]] - 1
        for k in contents[c]:
            keys[k] = keys.get(k, 0) + 1
        del locks[c]
    return " ".join([ str(i) for i in s ])

ncases = int(getline())

for casenr in range(1, ncases+1):
    k, n = [ int(s) for s in getline().split() ]
    keys = [ int(s) for s in getline().split() ]
    locks = {}
    contents = {}
    for i in range(n):
        arr = [ int(s) for s in getline().split() ]
        locks[i] = arr[0]
        contents[i] = arr[2:]
    emit("Case #%d: %s\n", casenr, solve(keys, locks, contents))
