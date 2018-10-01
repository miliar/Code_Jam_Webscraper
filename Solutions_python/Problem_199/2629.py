import sys
import math
	
def flip( cake_list, start, stop, step ):
	#print( "before flip : " + str(cake_list) + "start = %d, stop = %d, step = %d" % ( start, stop, step ) )
	for i in range( start, stop, step ):
		if cake_list[i] == '-':
			cake_list[i] = '+'
		else:
			cake_list[i] = '-'
	#print( "after flip cake : " + str(cake_list) )
	return cake_list
	
def get_flip_count_brute(pancake, K):
	cake_list = list(pancake)
	num_cakes = len(cake_list)
	
	flip_count = 0
	isReverseOrder = False
	index = 0
	r_index = num_cakes - 1
	while index < r_index:
		if isReverseOrder == False:
			if cake_list[index] == '-':
				if num_cakes - index < K :
					return 'IMPOSSIBLE'
				cake_list = flip( cake_list, index, index+K, 1 )
				flip_count += 1
				isReverseOrder = True
			index += 1	
		else:
			if cake_list[r_index] == '-':
				if r_index + 1 < K:
					return 'IMPOSSIBLE'
				cake_list = flip( cake_list, r_index, r_index-K, -1 )
				flip_count += 1
				isReverseOrder = False
			r_index -= 1	
			
	for ch in cake_list:
		if ch == '-':
			return 'IMPOSSIBLE'
	
	result = str(flip_count)
	return result

def main():
	#fr = open('pancake_small.txt', 'r')
	fr = open('A-large.in', 'r')
	fw = open('pancake_large_answer.txt', 'w')
	T = int(fr.readline())
	print( "%d test cases" % T)
	for i in range(T):
		cake, pan_size = [str(val) for val in fr.readline().split(' ')]
		K = int(pan_size)
		print( "pancake :%s, size:%d" % (cake, K))
		
		result = get_flip_count_brute(cake, K)
		
		print("Case #"+str(i+1)+": "+result)
		fw.write("Case #"+str(i+1)+": "+result+"\n")
	fr.close()
	fw.close()

if __name__ == '__main__':
	main()

