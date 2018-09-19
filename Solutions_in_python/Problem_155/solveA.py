import sys

assert( len(sys.argv)==3 )

def solve_task( data ):
	standing = 0
	invite = 0
	for shyness, ppl in enumerate(data):
		ppl = int(ppl)
		if standing <= shyness:
			need_to_invite = shyness-standing
			invite += need_to_invite
			standing += need_to_invite
		standing += ppl
	return invite


inp = open(sys.argv[1],"r")
inp.readline() # skip first
outp = open(sys.argv[2],"w")

for idx, line in enumerate( inp ):
	parts = line.strip().split()
	count = int(parts[0])
	data = parts[1]
	assert( len(data)==count+1 )
	solution = solve_task( data )
	solution_line = "Case #%i: %i\n" %( idx+1, solution )
	print solution_line,
	outp.write( solution_line )