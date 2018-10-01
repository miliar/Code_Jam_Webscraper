# ------------------------------------------------------------------------------
# globals
# ------------------------------------------------------------------------------
def pmatrix(a):
	for i in a:
		print i

def scan_diffheights(a):
	result = set()
	lines = range(len(a))
	cols = range(len(a[0]))

	for i in lines:
		for j in cols:
			result.add(a[i][j])
	return sorted(list(result), reverse=True)

def cut(a, height, cutlines=[], cutcols=[], full=False):
	lines = range(len(a))
	cols = range(len(a[0]))

	if full:
		for i in lines:
			for j in cols:
				a[i][j] = height
		return a

	if cutlines:
		for i in cutlines:
			for j in cols:
				a[i][j] = height
	if cutcols:
		for i in lines:
			for j in cutcols:
				a[i][j] = height
	return a

def checkncut_lines(height, plan, lawn):
	lines = range(len(plan))
	cols = range(len(plan[0]))
	need = set()
	cant_flag = False

	for i in lines:
		try:
			plan[i].index(height)
			need.add(i)
		except:
			continue

	# Got the required lines, check feasibility
	if need:
		for i in list(need):
			for j in cols:
				if plan[i][j] > height:
					cant_flag = True

			if not cant_flag:
				lawn = cut(lawn, height, cutlines=[i])
			cant_flag = False
	return lawn

def checkncut_cols(height, plan, lawn):
	plan = [list(tup) for tup in zip(*plan)]
	lawn = [list(tup) for tup in zip(*lawn)] # transpose
	lawn = checkncut_lines(height, plan, lawn)
	lawn = [list(tup) for tup in zip(*lawn)] # transpose
	return lawn


def check_feasibilityncut(height, plan, lawn):
	lawn = checkncut_lines(height, plan, lawn)
	lawn = checkncut_cols(height, plan, lawn)
	return lawn

# ------------------------------------------------------------------------------
# solution
# ------------------------------------------------------------------------------

f = open('in')
fo = open('out', 'w')

for T in range(int(f.readline())):
	dim = map(int, f.readline().strip().split())
	plan = [[100 for j in range(dim[1])] for i in range(dim[0])]
	lawn = [[100 for j in range(dim[1])] for i in range(dim[0])]
	for i in range(dim[0]):
		plan[i] = f.readline().strip().split()
	result = ""

	# Scan heights
	heights = scan_diffheights(plan)

	# First cut
	lawn = cut(lawn, max(heights), full=True)

	# Remove heighest height
	heights.pop(heights.index(max(heights)))
	if heights:
		for h in heights:
			lawn = check_feasibilityncut(h, plan, lawn)
			if h == heights[-1]:
				result = plan == lawn

	else:
		result = plan == lawn
	if result:
		print 'Case #%d: %s' % (T+1, "YES")
		fo.write('Case #%d: %s\n' % (T+1, "YES"))
		continue
	print 'Case #%d: %s' % (T+1, "NO")
	fo.write('Case #%d: %s\n' % (T+1, "NO"))


fo.close()
f.close()
