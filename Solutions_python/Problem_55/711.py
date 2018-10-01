#Codejam 5/8
#Theme park
#themepark.py

import re

file_in = "C-small-attempt2.in"
file_out = "C-small.out"

#Variables
# k people limit per ride
k = 0
# R runs of coaster
R = 0
# N groups of people
N = 0
# Queue of groups
groups = []
# money made
money = 0

def main():
	#Open file
	f = open(file_in)
	out = open(file_out, 'w')
	args = re.split(' ', f.readline())
	T = int(args[0])

	for t in xrange(T):
		#get vars
		args = re.split(' ', f.readline())
		R=int(args[0])
		k=int(args[1])
		N=int(args[2])
		#print 'r,k,n', R,k,N
		
		#make groups list
		groups = []
		group_list = re.split(' ', f.readline())
		for num_group in group_list:
			groups.append(int(num_group))
		#print 'groups', groups
		
		#start runs
		money = 0
		for i in xrange(R):
			#take dudes on coaster up to limit
			sofar = 0
			on_coaster = []
			while sofar <= k and len(groups):
				if sofar + groups[0] > k: break
				else:
					sofar += groups[0]
					on_coaster.append(groups.pop(0))
		
			#make them pay
			money += sofar
			#dudes go to back of queue
			for g in on_coaster:
				groups.append(g)
				
			#print groups
			
		out.write('Case #%d: %d\n' % (t+1, money))
	f.close()
	out.close()
			
		
		
	#print 'done'
		
if __name__ == "__main__":
	main()