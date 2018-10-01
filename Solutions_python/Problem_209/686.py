import sys
import collections
import math
import itertools


def calc_area(pcs):
	# calculate the total area of a list of pancakes, sorted by radius descending
	total = 0
	for i in range(len(pcs)-1):
		total += pcs[i]["total"] - pcs[i+1]["top"]
	total += pcs[len(pcs)-1]["total"]
	return total

def combine(pcs, area):
	p1 = pcs[0]
	p2 = pcs[1]
	
	return {"r": min(p1["r"], p2["r"]), "total": area, "top": min(p1["top"], p2["top"]), "id": p1["id"] + p2["id"]}

def run(N, K, pancakes, comb_pancakes):
	#choose K from N, maximize area
	#print(N)
	#print(K)
	#print(pancakes)
	if K == 1:
		return max(pancakes, key=lambda p: p["total"])["total"]
	if K == N:
		sort = sorted(pancakes, key=lambda p: p["r"], reverse=True)
		return calc_area(sort)
	
	# try to find pairs, that maximize the total area...
	max_area = 0
	max_comb = {}
	comb_pcs = []
	
	for comb in list(itertools.product(comb_pancakes, pancakes)):
		# don't use pancakes twice and make sure the order is correct
		if len(set(comb[0]["id"]).intersection(comb[1]["id"])) == 0 and comb[0]["r"] >= comb[1]["r"]:
			area = calc_area(comb)
			this_comb = combine(comb, area)
			comb_pcs.append(this_comb)
			if area > max_area:
				max_comb = this_comb
				max_area = area
			if area == max_area:				
				if this_comb["r"] > max_comb["r"]:
					max_comb = this_comb
	
	#print(pancakes)
	#print(comb_pcs)
	
	if len(max_comb["id"]) == K:
		return max_comb["total"]
	else:
		return run(N, K, pancakes, comb_pcs)
		

with open(sys.argv[1]) as f:
	lines = f.readlines()

with open("outA.txt", "w") as f:
	i = 1
	c = 1
	while i < len(lines)-1:
		# first line
		arr = list(map(int, lines[i].split()))
		N = arr[0]
		K = arr[1]
		pancakes = []
		i += 1
		
		for j in range(1,N+1):
			arr = list(map(int, lines[i].split()))
			pancakes.append({"r": arr[0], "h": arr[1], "top": arr[0]**2, "side": 2*arr[0]*arr[1], "total": arr[0]**2 + 2*arr[0]*arr[1], "id": [j]})
			i += 1
		
		#horses = collections.OrderedDict(sorted(horses.items(), key=lambda t: t[0]))
		
		res = math.pi*run(N,K,pancakes, pancakes)
		f.write("Case #{}: {}\n".format(c, round(res,9)))
		print("Case #{}: {}".format(c, round(res,9)))
		c += 1
