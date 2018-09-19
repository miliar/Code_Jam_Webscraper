#! c:\python33\python.exe

import sys
from collections import deque
import math

def calcMoveGap( mote, next_target ):

	gap_len = 0
	while mote <= next_target:
		mote *= 2
		mote -= 1
		gap_len += 1
		
	return mote, gap_len

def fewestChanges( mote, targets, add_cost, current_min ):

	while( len(targets) > 0 ):
		#print( "mote {} targets {} add_cost {} current_min {}".format(
		#		mote, targets, add_cost, current_min ) )
		if mote > targets[0]:
			mote += targets.popleft()
			current_min = min( current_min,
								add_cost + len( targets ) )
			continue
			
		gap_mote, gap_len = calcMoveGap( mote, targets[0] )
		current_min = min( current_min, add_cost + len( targets ) )
		
		if gap_len >= len(targets):
			return current_min
			
		add_cost += gap_len
		mote = gap_mote
							
		
	if add_cost == 0:
		return 0
		
	return current_min
	

def solve( input ):
	mote, target_ct = input.readline().rstrip().split()
	mote, target_ct = list( map( int, (mote,target_ct)))
	
	targets = input.readline().rstrip().split()
	targets = list( map( int, targets ) )
	targets.sort()
	targets = deque( targets )
	
	if mote < 2:
		return len( targets )
	
	return fewestChanges( mote, targets, 0, len( targets ) )


if __name__ == '__main__':
	input = open( sys.argv[1], "r" )
	output = open( sys.argv[2], "w" )
	
	tc_count = int( input.readline().rstrip() )
	
	for tc in range( 1, tc_count + 1):
		print( "Solving case: {}".format( tc ) )
		
		output.write( "Case #{}: {}\n".format( tc, solve( input ) ) )
	