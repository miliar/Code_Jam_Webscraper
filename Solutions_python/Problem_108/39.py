#!/usr/bin/python
import sys
import math


def vines_near(vines, current_vine, reach_maxpos):
	result = []
	for i in xrange(current_vine + 1, len(vines)):
		(d,l) = vines[i]
		if (d <= reach_maxpos):
			result.append(i)
	#print "vines_near",current_vine,reach_maxpos, result
	result.reverse()
	return result
	
def is_possible(vines,distance):
	(d,l)=vines[0]
	return is_possible_rec(vines, distance, d, 0, d)

def is_possible_rec(vines, distance, current_position, current_vine, current_reach):
	#print "is_possible_rec dist", distance, "pos", current_position, "vine",current_vine, "reach",current_reach
	
	(current_d, current_l) = vines[current_vine]
	
	reach_maxpos = min(current_position + current_reach, current_position + current_l)
	
	if (reach_maxpos >= distance):
		return True
	
	
	
	near = vines_near(vines, current_vine, reach_maxpos)
	for new_vine in near:
		#print "testing:",new_vine,vines[new_vine]
		(new_d, new_l) = vines[new_vine]
		new_reach = new_d - current_d
		
		#if (new_reach > new_l):
		#	print "Skipping vine",new_reach,new_l
		#	continue
			
		new_position = new_d
		
		if (is_possible_rec(vines, distance, new_position, new_vine, new_reach)):
			return True

	return False
	

def main():
	T = int(sys.stdin.readline())
	
	for i in xrange(T):
		parts = sys.stdin.readline().strip().split(' ')
		N = int(parts[0])
		
		vines = []
		for j in xrange(N):
			parts = sys.stdin.readline().strip().split(' ')
			Dj = int(parts[0])
			Lj = int(parts[1])
			vines.append((Dj,Lj))
		parts = sys.stdin.readline().strip().split(' ')
		distance = int(parts[0])
		
		##if (i != 2):
		#	continue
			
		#print vines,distance
		
		possible = is_possible(vines,distance)
		if (possible):
			possible_str = "YES"
		else:
			possible_str = "NO"
		print "Case #" + str(i+1) + ": " + possible_str
main()
