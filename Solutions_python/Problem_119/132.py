import sys

from math import log, floor, ceil, sqrt
from itertools import takewhile, imap, count
from multiprocessing import Pool

def add_keys(current, key_list):
	c = current.copy()
	for key_type in key_list:
		c[key_type] = c.get(key_type, 0) + 1
	
	return c

def use_key(current, key_type):
	c = current.copy()
	nr = c[key_type]
	if nr == 1:
		del c[key_type]
	elif nr > 1:
		c[key_type] = nr - 1
	else:
		raise Exception("%s => %s" % (key_type, nr))
	return c

def keys_inside_chests(chests):
	reducer = lambda acc, (chest_no, (chest_key, keys_inside)): add_keys(acc, keys_inside)
	return reduce(reducer, chests, {})

def keys_to_open_chests(chests):
	reducer = lambda acc, (chest_no, (chest_key, keys_inside)): add_keys(acc, [chest_key])
	return reduce(reducer, chests, {})

def chest_nos(chests):
	return set((chest_no for chest_no, (chest_key, keys_inside) in chests))

def can_be_opened(chest, keys, chests):
	chest_no, (key_type, keys_inside) = chest
	print >> debug_log, "Will check Ch %d of: %s" % (chest_no, chest_nos(chests))
	# print >> debug_log, "key_type: %d, keys: %s" % (key_type, keys)
	if key_type in keys:
		print >> debug_log, "Ch %d can be opened" % chest_no
		return True
	else:
		remaining_chests = filter(lambda (c_no, _): chest_no != c_no, chests)
		for other_chest in remaining_chests:
			if key_type in other_chest[1][1]:
				return can_be_opened(other_chest, add_keys(keys, keys_inside), remaining_chests)
		print >> debug_log, "Ch %d can't be opened, remaining: %s" % (chest_no, chest_nos(remaining_chests))
		return False

def possible_to_continue(keys, chests):
	if len(keys) == 0 and len(chests) > 0:
		# print >> debug_log, "no keys, still %s chests" % len(chests)
		return False

	keys_available = keys_inside_chests(chests)
	for key_type, count in keys.iteritems():
		keys_available[key_type] = keys_available.get(key_type, 0) + count
	
	keys_needed = keys_to_open_chests(chests)

	for key_type, count in keys_available.iteritems():
		if keys_needed.get(key_type, 0) > count:
			print >> debug_log, "Missing %d keys of type %d" % (keys_needed[key_type] - count, key_type)
			return False

	return all(map(lambda c: can_be_opened(c, keys, chests), chests))

def solve_(keys, chests, open_chests):
	print >> debug_log, "Open: %s" % open_chests

	if not possible_to_continue(keys, chests):
		return None
	
	if len(chests) == 0:
		return open_chests

	for chest_no, (chest_key, keys_inside) in chests:
		if chest_key in keys:
			print >> debug_log, "My keys: %s, opening %d with %d" % (keys, chest_no, chest_key)
			my_keys = add_keys(use_key(keys, chest_key), keys_inside)
			remaining_chests = filter(lambda (c_no, _): chest_no != c_no, chests)
			solution = solve_(my_keys, remaining_chests, open_chests + [chest_no])
			if solution is not None:
				return solution
	
	print >> debug_log, "Boo", keys, chest_nos(chests)
	return None

def solve((start_keys, chests)):
	print >> debug_log, "Starting keys", start_keys
	print >> debug_log, "All chests"
	for c_n, c_d in chests:
		print >> debug_log, "chest no. %d: %s" % (c_n, c_d)
	solution = solve_(start_keys, chests, [])
	if solution is None:
		return "IMPOSSIBLE"
	else:
		return " ".join(map(str, solution))

def parse_chest(inp):
	line = map(int, next(inp).split())
	key_type = line[0]
	n_keys = line[1]
	keys = line[2:]
	assert len(keys) == n_keys
	return (key_type, keys)

def parse_case(inp):
	k, n = map(int, next(inp).split())
	
	start_keys = map(int, next(inp).split())
	assert len(start_keys) == k

	start_key_map = add_keys({}, start_keys)

	chests = [(i + 1, parse_chest(inp)) for i in range(n)]
	return (start_key_map, chests)
	
def parse(fileName):
	with open(fileName) as f:
		cases = int(next(f))

		cases_inp = [parse_case(f) for i in range(cases)]
		next_line = f.readline()
		assert "" == next_line, "Unexpected line: %s" % next_line
	
	pool = Pool(8)
#       result = pool.imap(solve, cases_inp, 1)
	result = imap(solve, cases_inp)
	return result

if __name__ == "__main__":
	with open("debug-log.out", "w") as debug_log:
		for (i, result) in enumerate(parse(sys.argv[1])):
			print >> sys.stderr, "Case #%d: %s" % (i + 1, result)
			print >> debug_log, "Case #%d: %s" % (i + 1, result)
			print "Case #%d: %s" % (i + 1, result)
