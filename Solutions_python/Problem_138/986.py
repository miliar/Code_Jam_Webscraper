tests = int(raw_input())


def play_war(naomi, ken):
	naomi_score = 0
	naomi.sort()
	ken.sort()
	rounds = len(naomi)

	while len(naomi) > 0:
		rounds -= 1
		h_n = naomi[rounds]
		h_k = ken[rounds]
		l_k = ken[0]

		if h_n > h_k:
			naomi_score += 1
			naomi.remove(h_n)
			ken.remove(l_k)
		else:
			naomi.remove(h_n)
			ken.remove(h_k)
			
	return naomi_score

def index_greater_than(array, value):
	for x in range(len(array)):
		if array[x] > value:
			return x
	return -1

def play_d_war(naomi, ken):
	naomi_score = 0
	naomi.sort()
	ken.sort()
	rounds = len(naomi)

	while len(naomi) > 0:
		rounds -= 1
		h_n = naomi[rounds]
		h_k = ken[rounds]
		l_n = naomi[0]
		l_k = ken[0]
		
		chosen_one = index_greater_than(naomi, h_k)

		if chosen_one >= 0:
			naomi_score += 1
			naomi.remove(naomi[chosen_one])
			ken.remove(h_k)
		else:
			naomi.remove(l_n)
			ken.remove(h_k)
			
	return naomi_score

for i in range(tests):
	rounds = input()

	naomi = [float(x) for x in raw_input().split(" ")]
	ken = [float(x) for x in raw_input().split(" ")]
	naomi2 = naomi[:]
	ken2 = ken[:]

	war_points = play_war(naomi, ken)
	d_war_points = play_d_war(naomi2, ken2)

	print "Case #" + str(i+1) + ": " + str(d_war_points) + " " + str(war_points)


#Input 
 	
# 4
# 1
# 0.5
# 0.6
# 2
# 0.7 0.2
# 0.8 0.3
# 3
# 0.5 0.1 0.9
# 0.6 0.4 0.3
# 9
# 0.186 0.389 0.907 0.832 0.959 0.557 0.300 0.992 0.899
# 0.916 0.728 0.271 0.520 0.700 0.521 0.215 0.341 0.458

# Output 
 
# Case #1: 0 0
# Case #2: 1 0
# Case #3: 2 1
# Case #4: 8 4
