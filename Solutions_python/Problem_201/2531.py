import sys
import math

def calc_stalls(n, k):
	empty_stalls = [True for x in range(n)]
	halves = [[0, n - 1, n]]
	for person in range(k):
		max_half_value = max([half[2] for half in halves])
		max_half_pos = [pos for pos,x in enumerate(halves) if x[2] == max_half_value][0]
		#print(max_half_pos)
		max_half = halves[max_half_pos]
		#print(max_half)
		if (max_half[2]%2==0):
			new_pos = (max_half[1] - max_half[0]) // 2
		else:
			new_pos = math.ceil((max_half[1] - max_half[0])/2)
		new_pos = max_half[0] + new_pos
		empty_stalls[new_pos] = False
		#print("new_pos: " + str(new_pos))
		del halves[max_half_pos]
		halves.append([max_half[0], new_pos -1, (new_pos - max_half[0])])
		halves.append([new_pos + 1, max_half[1], (max_half[1] - new_pos)])
		#print(halves)

	return calc_tuple(empty_stalls, new_pos)

def calc_tuple(empty_stalls, pos):
	ls = 0
	rs = 0
	for x in reversed(empty_stalls[0:pos]):
		if x:
			ls += 1
		else: 
			break
	for x in empty_stalls[pos+1:]:
		if x:
			rs += 1
		else: 
			break

	#ls = sum(x for x in empty_stalls[0:pos] if x)
	#rs = sum(x for x in empty_stalls[pos+1:] if x)
	return (ls, rs)

if __name__ == '__main__':
    num_cases = int(sys.stdin.readline().strip())
    case = 0
    while True:
        case += 1
        line = sys.stdin.readline().strip()
        if line == '':
            break
        n,k = [int(x) for x in line.split()]
        #print("n: " + str(n) + "k: " + str(k))
        chosen = calc_stalls(n, k)
        print("Case #" + str(case) + ": " + str(chosen[1]) + " " + str(chosen[0]))