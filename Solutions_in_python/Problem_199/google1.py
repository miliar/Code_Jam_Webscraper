import sys
max_trycount = 100
## input output part ----------------##
def read_input():
	input = {}
	with open(sys.argv[1],"r") as f:
		data = f.readlines()

	input["testcount"] = int(data.pop(0))
	tests =[]
	for line in data:
		c, K = line.strip().split(" ")
		tests.append((c,int(K)))
	
	input["tests"] = tests
	return input


def save_output(results):
	with open("output.txt", "w") as f:
		for result in results:
			print "Case: #{}: {}\n".format(result["case"],result["result"])
			f.write("Case #{}: {}\n".format(result["case"],result["result"]))

## end of input output part ----------------##

## ---- helper functions  ----------------##
def flip_pc(p,start_index,K):
	p[start_index:start_index+K] =  [not x for x in p[start_index:start_index+K] ]
	return p

def convert(pancake):
	pancakes = []
	for p in pancake:
		if p == "-":
			pancakes.append(False)
		elif p == "+":
			pancakes.append(True)
	return pancakes


## ---- end of helper functions  ----------------##

## ---- runner  ----------------##
def run(input):
	results = []
	for case in range(1,input["testcount"]+1):
		results.append({"case":case, "result": test_cases(input["tests"][case-1])})

	return results

def test_case(p,K,tc=0):
	print "t:{},K:{},tc:{}".format(p,K,tc)
	if tc > max_trycount:
		return "IMPOSSIBLE"
	if all(p):
		return tc
	#find first -
	fn = p.index(False)
	print "fn:",fn
	if (fn + K <= len(p)):
		#check if next K-1 same
		if not any(p[fn:fn+K]):
			p = flip_pc(p,fn,K)
			tc +=1
			return test_case(p,K,tc)
		else:
			# find first + after -
			fpn = p[fn:].index(True)
			print "fpn:", fpn
			fp = fn +fpn
			print "fp:", fp
			if (fp + K <= len(p)):
				p = flip_pc(p,fp,K)
				tc +=1
				return test_case(p,K,tc)

	return "IMPOSSIBLE"

def test_cases(test):
	x, K = test
	p = convert(x)
	if all(p):
		return 0

	if K == len(p):
		if not any(p):
			return 1
		else:
			return "IMPOSSIBLE"

	return test_case(p,K)

if __name__ == "__main__":
	input = read_input()
	#print "input:", input
	results = run(input)
	print "results:", results
	#results = [{"case":1, "result": 3},{"case":1, "result": 1},{"case":1, "result": "Impossible"}]
	save_output(results)


