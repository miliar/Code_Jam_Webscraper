def Flip(start,end):
	# print start, end
	for i in range(start,end):
		S[i] = '+' if S[i] == '-' else '-'

T = int(raw_input())

for i in range(T):
	S,K = raw_input().split()
	S = list(S)
	C = 0

	for j in range(0,len(S)):
		try:
			index = S.index('-')
			if(index + int(K) > len(S)):
				break
			else:				
				Flip(index,index+int(K))
				C = C + 1
		except ValueError:
			break
		

	try:
		index = S.index('-')
		C = 'IMPOSSIBLE'    
	except ValueError:
		pass

	print 'Case #'+str(i+1)+': '+ str(C)