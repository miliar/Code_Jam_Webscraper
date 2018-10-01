def calcInvitees(standing, audience, shyness):
	if len(audience) == 1:
		return 0
	standing += audience[0]
	shyness += 1
	if standing >= shyness:
		return calcInvitees(standing, audience[1:], shyness)
	return (shyness - standing) + calcInvitees(shyness, audience[1:], shyness)

def main():
	caseCount = int(input())
	for caseNum in range(caseCount):
		caseValues = input().split()
		maxShyness = int(caseValues[0])
		initialStanding = 0
		audienceShyness = [int(people) for people in caseValues[1]]
		initialShyness = 0
		inviteeCount = calcInvitees(initialStanding, audienceShyness, initialShyness)
		print("Case #{}: {}".format(caseNum + 1, inviteeCount))

if __name__ == "__main__":
	main()