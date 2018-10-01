def highest(score):
	normal,surprising = [],[]
	
	for i in range(11):
		for j in range(11):
			for k in range(11):
				if i+j+k == int(score) and abs(i-j)<2 and abs(i-k)<2 and abs(j-k)<2: normal.append((i,j,k))
				elif i+j+k == int(score) and abs(i-j)<3 and abs(i-k)<3 and abs(j-k)<3: surprising.append((i,j,k))
	
	maxScoreNormal = 0,-1
	for i in range(len(normal)):
		mMax = max(normal[i]),i
		if mMax[0]>maxScoreNormal[0]: maxScoreNormal = mMax
	
	maxScoreSurprising = 0,-1
	for i in range(len(surprising)):
		mMax = max(surprising[i]),i
		if mMax[0]>maxScoreSurprising[0]: maxScoreSurprising = mMax
	
	tScore = [0,0]
	if len(normal) > 0: tScore[0] = max(normal[maxScoreNormal[1]])
	if len(surprising) > 0: tScore[1] = max(surprising[maxScoreSurprising[1]])
	return tScore


def check(scores,p,S):
	
	normalScores,surprisingScores = [],[]
	
	for i in range(len(scores)):
		normalScores.append(scores[i][0])
		surprisingScores.append(scores[i][1])
	
	ramp = 0
	for i in range(len(scores)):
		if normalScores[i]<p and surprisingScores[i]>=p and ramp<S:
			normalScores[i] = surprisingScores[i]
			ramp = ramp+1
	#normalScores[normalScores.index(min(normalScores))] = surprisingScores[normalScores.index(min(normalScores))]
	#normalScores[normalScores.index(min(normalScores))] = surprisingScores[normalScores.index(min(normalScores))]
	
	count = 0
	for i in range(len(normalScores)):
		if normalScores[i] >= p: count = count+1
		
	#print(normalScores)
	#print(surprisingScores)
	return count
	
	 
T = raw_input()
out,i='',1

for k in range(int(T)):
	maxScores = []
	minput = raw_input()
	N,S,p,scores = minput.split(' ')[0], minput.split(' ')[1], minput.split(' ')[2], minput.split(' ',3)[3].split(' ')
	for i in range(len(scores)):
		maxScores.append(highest(scores[i]))
	
	#print(maxScores)
	out += 'Case #' + str(k+1) + ': ' + str(check(maxScores,int(p),int(S)))
	if (k+1)<T: out += '\n'

print(out)