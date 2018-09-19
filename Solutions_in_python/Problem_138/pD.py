""" Chad Reynolds 4/11/14

Google Code Jam 2014
Qualifying Round
Problem D

Elapsed time from beginning to submission:  
"""
import sys

if __name__ == "__main__":

	input = sys.argv[1]
	output = sys.argv[2]

	output = open(output, "w")
	file = open(input, "r")
	num_cases = int(file.readline())

	## problem ##
	for i in range(num_cases):
		# arrange blocks
		num_blocks = int(file.readline())
		n = file.readline().rstrip().split(" ")
		k = file.readline().rstrip().split(" ")
		n.sort()
		k.sort()
		k2 = sorted(k)
		
		print("\nGame {2}  Number of Blocks: {3}\nN = {0}\nK = {1}".format(n, k, i+1, num_blocks))

		# play war
		print("\nWar:")
		n_points = 0
		for j in range(num_blocks):
			n_play = n[j]
			for l in range(num_blocks):
				if l >= len(k):
					k_play = k[0]
					#n_points += 1
					break
				else:
					k_play = k[l]
					if k_play > n_play:
						break
					else:
						k_play = k[0]

			if k_play < n_play:
				n_points += 1

			print("Round {0}:  N play = {1}  K play = {2}  N score = {3}".format(j+1, n_play, k_play, n_points))
			k.remove(k_play)
			print("New K = " + str(k))
		z = n_points
			
		# play deceitful war
		print("\nDeceitful War:\nN = {0}\nK = {1}".format(n, k2))
		j = 0
		while j < len(n):
			if n[j] < k2[j]:
				print("Popping.")
				n.pop(0)
				k2.pop(len(k2)-1)
			else:
				j += 1
				
		print("Final lists:\nN = {0}\nK = {1}".format(n, k2))
		y = len(n)
		
		# output answer
		print("Case #{0}: {1} {2}\n".format(i+1, y, z))
		output.write("Case #{0}: {1} {2}\n".format(i+1, y, z))	

	output.close()	
	file.close()
