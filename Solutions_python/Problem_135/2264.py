import sys

def case (case_num):
	set1 = None
	set2 = None
	
	row_num = int(raw_input())
	
	for i in xrange( 1, 5 ):
		row = sys.stdin.readline().strip()
		
		if i == row_num:
			set1 = set( row.split() )
	
	row_num = int(raw_input())
	
	for i in xrange( 1, 5 ):
		row = sys.stdin.readline().strip()
		
		if i == row_num:
			set2 = set( row.split() )

	final_set = set1.intersection(set2)
	
	dialog = "Case #" + str(case_num) + ": "
	if len(final_set) == 0:
		dialog = dialog + "Volunteer cheated!"
	elif len(final_set) == 1:
		dialog = dialog + str(final_set.pop())
	else:
		dialog = dialog + "Bad magician!"

	print dialog

if __name__ == "__main__":
	num_cases = int(raw_input())

	for i in xrange( 1, num_cases + 1 ):
		case(i)




