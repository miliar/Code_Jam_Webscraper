import sys
import os

in_file = str(sys.argv[1]) 
out_file = os.path.splitext(in_file)[0] + '.out'

fin = open(in_file, 'r')
nr_of_cases = int(fin.readline())

fout = open(out_file, 'w')

cases_done = 0

def deceitful_war_points(naomi_blocks, ken_blocks):
	naomi_points = 0
	
	while naomi_blocks:
		if naomi_blocks[-1] > ken_blocks[-1]:
			naomi_points += 1
			kb_min = ken_blocks.pop(0)
			for i in xrange(len(naomi_blocks)):
				if naomi_blocks[i] > kb_min:
					naomi_blocks.pop(i)
					break
		else:
			ken_blocks.pop()
			naomi_blocks.pop(0)
	
	return naomi_points

def war_points(naomi_blocks, ken_blocks):
	naomi_points = 0
	for nb in naomi_blocks:
		found = False
		for i in xrange(len(ken_blocks)):
			if ken_blocks[i] > nb:
				found = True
				ken_blocks.pop(i)
				break
		if not found:
			ken_blocks.pop(0)
			naomi_points += 1
			
	return naomi_points

while cases_done < nr_of_cases:
	cases_done += 1
	
	fin.readline()
	
	naomi_blocks = map(float, fin.readline().split())
	ken_blocks = map(float, fin.readline().split())
	
	naomi_blocks.sort()
	ken_blocks.sort()
	
	y = deceitful_war_points(list(naomi_blocks), list(ken_blocks))
	z = war_points(naomi_blocks, ken_blocks)
	
	fout.write('Case #{0}: '.format(cases_done))
	fout.write('{0} {1}'.format(y, z))
	fout.write('\n')
	
fin.close()
fout.close()
