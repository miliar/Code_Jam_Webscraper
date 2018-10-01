import sys

class Magicka:
	
	def __init__(self):
		t = int(sys.stdin.readline())
		for i in range(t):
			comb_rules, opp_rules, inv = self.read_case()
			soln = self.solve_case(comb_rules, opp_rules, inv)
			self.print_soln(i+1, soln)

	def print_soln(self, i, soln):
		sol_str = "Case #%i: %s"%(i, str(soln))
		print sol_str.replace("'", "")

	def read_case(self):
		ln = sys.stdin.readline().split()
		
		c = int(ln.pop(0))
		comb_rules = {}
		for i in range(c):
			self.add_comb_rule(comb_rules, ln.pop(0))
		
		d = int(ln.pop(0))
		opp_rules = {}
		for i in range(d):
			self.add_opp_rule(opp_rules, ln.pop(0))
		
		n = int(ln.pop(0))
		inv = ln.pop(0)
		
		return comb_rules, opp_rules, inv
		

	def add_comb_rule(self, comb_rules, rule_str):
		comb_rules[rule_str[0]+rule_str[1]] = rule_str[2]
		comb_rules[rule_str[1]+rule_str[0]] = rule_str[2]

	def add_opp_rule(self, opp_rules, rule_str):
		a = rule_str[0]
		b = rule_str[1]
		if opp_rules.has_key(a):
			opp_rules[a].append(b)
		else:
			opp_rules[a] = [b]
		if opp_rules.has_key(b):
			opp_rules[b].append(a)
		else:
			opp_rules[b] = [a]

	def check_comb_rules(self, c_rules, el, hist):
		a = el[-2]
		b = el[-1]
		k = a + b
		if c_rules.has_key(k):
			c = c_rules[k]
			el.pop()
			el[len(el) - 1] = c
			self.hist_remove(hist, a)
			self.hist_remove(hist, b)
			self.hist_add(hist, c)
			self.dbg("%s,%s->%s "%(a,b,c))
		return el, hist

	def check_opp_rules(self, o_rules, el, hist):
		k = el[-1]
		if o_rules.has_key(k):
			for c in o_rules[k]:
				if hist.has_key(c):
					self.dbg("%s*%s "%(c,k))
					el = []
					hist = {}
		return el, hist

	def hist_remove(self, hist, e):
		if 1 == hist[e]:
			del hist[e]
		else:
			hist[e] -= 1

	def hist_add(self, hist, e):
		if hist.has_key(e):
			hist[e] += 1
		else:
			hist[e] = 1

	def solve_case(self, c_rules, o_rules, inv):
		el = []
		hist = {}
		for e in inv:
			el.append(e)
			self.dbg("\n"+str(el))
			self.hist_add(hist, e)
			if len(el) > 1:
				el, hist = self.check_comb_rules(c_rules, el, hist)
				el, hist = self.check_opp_rules(o_rules, el, hist)
		self.dbg('\n'+str(hist))
		return el

	def dbg(self, msg):
		#print msg,
		return

if __name__ == "__main__":
	Magicka()
