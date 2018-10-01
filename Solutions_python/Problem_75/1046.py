def solve_case(case):
	cur = 0
	case = case.split(' ')
	comb_rules = []
	tot_comb_rules = int(case[cur])
	for i in range(1, tot_comb_rules+1):
		cur += i
		comb_rules.append((case[cur][:2], case[cur][2]))
	cur += 1
	elem_rules = []
	for i in range(1, int(case[cur])+1):
		cur += i
		elem_rules.append(case[cur])
	
	inp_len = int(case[cur + 1])
	inp = case[cur + 2]
	out = []
	applied_rule = False
	for i in range(inp_len):
		if len(out) == 0:
			out.append(inp[i])
			continue
		if(applied_rule):
			applied_rule = False
		else:
			for rule in comb_rules:
				if rule[0] == out[-1]+inp[i] or rule[0] == inp[i]+out[-1]:
					out.pop()
					out.append(rule[1])
					applied_rule = True
					break;
		if(applied_rule):
			continue
		for rule in elem_rules:
			if (rule[0] == inp[i] and rule[1] in out) or (rule[1] == inp[i] and rule[0] in out):
				out = []
		if len(out) != 0:
			out.append(inp[i])
	
	return "["+', '.join(out)+"]"
		
		
		

fin = open('input11.txt')
fout = open('out11.txt','w')

inp = fin.readlines()
tot_case = int(inp[0])
for i in range(1, tot_case+1):
	fout.write("Case #" + str(i) + ": " + solve_case(inp[i]) + "\n")
	
fin.close()
fout.close()