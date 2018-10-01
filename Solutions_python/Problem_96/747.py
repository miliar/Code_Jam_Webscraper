
# def split_score(score):
# 	triplet = [score // 3]
# 	for i in xrange(2, 0, -1):
# 		score -= triplet[-1]
# 		triplet.append(score // i)
# 	return triplet


# test_cases = int(raw_input())
# for test in xrange(1, test_cases + 1):
# 	scores = [int(e) for e in raw_input().split()]
# 	googlers = scores.pop(0)
# 	surprising = scores.pop(0)
# 	p = scores.pop(0)
# 	better_googlers = 0
# 	scores.sort()
# 	for score in scores:
# 		triplet = split_score(score)
# 		if surprising and score > 1 and triplet[2] + 1 == p:
# 			triplet[2] += 1
# 			surprising -= 1
# 		if triplet[2] >= p:
# 			better_googlers += 1
# 	print 'Case #%d: %d' % (test, better_googlers)




triplets = {}

def split_score(score):
	triplet = []
	for i in xrange(3, 0, -1):
		triplet.append(score // i)
		score -= triplet[-1]
	return triplet


def make_triplets():
	for n in xrange(31):
		triplets[n] = split_score(n)


def main():
	make_triplets()
	test_cases = int(raw_input())
	for test in xrange(1, test_cases + 1):
		scores = [int(e) for e in raw_input().split()]
		googlers = scores.pop(0)
		surprising = scores.pop(0)
		p = scores.pop(0)
		scores.sort()
		best_googlers = 0
		for score in scores:
			if surprising and score % 3 != 1 and score > 1 and triplets[score][2] + 1 >= p:
				best_googlers += 1
				surprising -= 1
			elif triplets[score][2] >= p:
				best_googlers += 1
		print 'Case #%d: %d' % (test, best_googlers)


main()
