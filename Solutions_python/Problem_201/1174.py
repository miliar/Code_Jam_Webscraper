import sys

def choose2(n, k):
	max_seq_list = [n]
	max_seq_times = {n : 1}
	while(k!=0):
		max_seq = max_seq_list[-1]
		if max_seq == 1:
			return "0 0"
		
		for j in range(max_seq_times[max_seq]):
			if max_seq % 2 == 0:
				ls = max_seq/2 - 1
				rs = max_seq/2
			else:
				ls = max_seq/2
				rs = max_seq/2
				
			if ls in max_seq_times:
				max_seq_times[ls]+=1
			else:
				max_seq_times[ls]=1
				max_seq_list.append(ls)
				
			if rs in max_seq_times:
				max_seq_times[rs]+=1
			else:
				max_seq_times[rs]=1
				max_seq_list.append(rs)
				
			max_seq_list = sorted(max_seq_list)
			k-=1
			if(k==0):
				return " ".join(str(i) for i in [rs, ls])
		
		max_seq_list.pop(-1)
		max_seq_times.pop(max_seq, None)

def choose(n, k):
	state = sorted([n])
	ls=rs=0
	for i in range(k):
		max_seq = state[-1]
		if max_seq % 2 == 0:
			ls = max_seq/2 - 1
			rs = max_seq/2
			state.append(max_seq/2 - 1)
			state.append(max_seq/2)
		else:
			ls = max_seq/2
			rs = max_seq/2
			state.append(max_seq/2)
			state.append(max_seq/2)
		
		state = sorted(state)
		state.pop(-1)
		
	return " ".join(str(i) for i in [rs, ls])

def run_case(case_params):
	case_params = case_params.strip().split(" ")
	n = int(case_params[0])
	k = int(case_params[1])
	return choose2(n, k)
	
def main():
	input = open(sys.argv[1], 'rb').readlines()
	number_of_cases = int(input[0])
	cases = input[1:number_of_cases+1]
	
	for i, case in enumerate(cases):
		ans = run_case(case)
		print "Case #%d: %s" % (i+1, ans)
		
if __name__ == "__main__":
	main()