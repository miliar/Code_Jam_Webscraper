#nanook

lines = [line.strip() for line in open('A-large.in')]

results = list()

testCases = int(lines[0])

for x in range(1, (testCases+1)):
	friendsNeeded = 0
	audienceMembers = 0

	tempAudience = (lines[x].split())
	
	individuals = list(tempAudience[1])
	individuals = [int(x) for x in individuals]
	
	for counter in range(0, len(individuals)) :
		audienceMembers += individuals[counter]
		
		while (audienceMembers + friendsNeeded) <= counter :	
			friendsNeeded += 1
		
	results.append("Case #%s: %s" % (str(x),str(friendsNeeded)))
	print ("solution", friendsNeeded)

print (results)

problem1aOutput = open('standingOvationLargeOutput.txt', 'w')

for item in results:
  problem1aOutput.write("%s\n" % item)
