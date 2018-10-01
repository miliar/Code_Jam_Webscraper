

import re;

T = int(input());


def get_next(queue):
	n = 0;
	for list in queue:
		if len(list) > 0:
			return [n, list.pop()];
		n += 1;
	
	return None;


def check(ps, k):
	if all(ps):
		return 0;
	
	c = len(ps);
	
	checked = {tuple(ps)};
	queue = [[ps]];
	
	while True:
		pair = get_next(queue);
		if pair == None:
			return None;
		n, ps = pair;
		n += 1;

		for i in range(0, c - k + 1):
			new_ps = []
			for j in range(0, i):
				new_ps.append(ps[j]);
			
			for j in range(i, i + k):
				new_ps.append(not ps[j]);
			
			for j in range(i + k, c):
				new_ps.append(ps[j]);
			
			if all(new_ps):
				return n;
			
			t_new_ps = tuple(new_ps);
			if not (t_new_ps in checked):
				checked.add(t_new_ps);
				depth = len(queue);
				while depth < n + 1:
					queue.append([]);
					depth += 1;
				queue[n].append(new_ps);
	
	return None;

for t in range(1, T + 1):
	l, k = input().strip().split(r" ");
	ps = [p == '+' for p in list(l)];
	k = int(k);
	
	output = "Case #" + str(t) + ": ";
	
	solution = check(ps, k);
	
	if solution != None:
		output += str(solution);
	else:
		output += "IMPOSSIBLE";
		
	print(output);
	
