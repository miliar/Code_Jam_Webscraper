"""
Written for Google Code Jam 2014
Kolijn Wolfaardt
kolijn.wolfaardt@gmail.com
"""

f = open('war/D-large.in','r')

T = int(f.readline())

for t in range(T):
	#Read the ammount of tiles. Not needed
	f.readline()
	#Read the line
	naomi = [float(a) for a in f.readline().split()]
	ken = [float(a) for a in f.readline().split()]

	naomi.sort() #Sort from small to large
	ken.sort() # Sort from large to small
	ken.reverse()

	naomiWar = naomi[:]
	kenWar = ken[:]

	naomiScore=0
	#print (naomi)
	#print (ken)
	
	#First, loop through from the end, play only if we have a larger number that the other guy
	while (len(naomi) > 0):
		cont=0
		while cont==0:

			length=len(naomi)-1
			if (len(naomi)>0 and naomi[length] > ken[0]): #We win this
				#remove them
				#print ("Playing fair  N {} K {}".format(naomi[length],ken[0]))
				naomi.pop(length)
				ken.pop(0)
				naomiScore = naomiScore+ 1
				cont=0
			else:
				cont=1

		#Both arrays have their biggest values up front now
		naomi.reverse()

		# Force Ken to play his biggest value (bigger than ours) but play our smallest
		cont = 1
		#While ken has larger values than us
		while (len(naomi)>0 and naomi[0] < ken[0]):
			#Force him to play his largest, and play our smallest
			#print ("Playing cheat N {} K {}".format(naomi[len(naomi)-1],ken[0]))
			naomi.pop(len(naomi)-1)
			ken.pop(0)
		naomi.reverse()
	


	#Now get the optimal war score
	naomiWar.sort()
	kenWar.sort()
	naomiWarScore =0

	#Play war optimally.
	#Start with the smallest value
	count =0
	while (count<len(naomiWar)):
		#find the value one larger in ken
		currPos=0
		while (currPos<len(naomiWar) and kenWar[currPos] < naomiWar[count]):
			currPos = currPos+1
	
		if (currPos >= len(naomiWar)):
			#We ain't found shit!
			#Play the smallest value we have. Gonna lose it anyway
			kenRemoveIndex = kenWar.index(min(kenWar))
			naomiWarScore = naomiWarScore+1
		else:
			kenRemoveIndex = currPos
		naomiWar.pop(count)
		kenWar.pop(kenRemoveIndex)

	
	print ("Case #{}: {} {}".format(t+1,naomiScore,naomiWarScore))
