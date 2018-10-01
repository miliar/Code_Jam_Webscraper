

def cost(a,b,n):
	if a >= b:
		return 0
	
	return (b-a) * n - ((b-a)*(b-a-1))//2 
	
	
def case():
	n,m = map(int,input().split())
	
	trips = []
	
	original_cost = 0
	
	for i in range(m):
		o,e,p = map(int,input().split())
		
		trips.append( (o,1,p) )
		trips.append( (e,2,p) )
		
		original_cost += cost(o,e,n) * p
		#original_cost %= 1000002013
		
	trips.sort()
	
	new_cost = 0
	
	passengers = []
	
	for t in trips:
		d,m,p = t
		
		if m == 1:
			passengers.append( [d,p] )
		elif m == 2:
			while p > 0:
				if passengers[-1][1] <= p:
					new_cost += cost(passengers[-1][0],d,n) * passengers[-1][1]
					p -= passengers[-1][1]
					del passengers[-1]
				else:
					new_cost += cost(passengers[-1][0],d,n) * p
					passengers[-1][1] -= p
					p = 0
				#new_cost %= 1000002013
			
	#print(original_cost, new_cost)
	
	return (original_cost - new_cost) % 1000002013
	
	
	
	
	
	
	
	
	
	
for t in range(1,int(input())+1):
	print ( "Case #%d: %d" % (t,case()) )