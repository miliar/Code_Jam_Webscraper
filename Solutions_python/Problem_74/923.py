def calc_sec( steps ):
	sec = 0
	Opos = 1
	Bpos = 1
	last_seco, last_secb = 0, 0
	last_bot = ''
	for i in steps:

		bot = i[0]
		pos = int(i[1])
		if bot == 'O':
			if last_secb > abs( pos-Opos ):
				now_time =  1
			else:
				now_time = abs( pos - Opos ) - last_secb + 1

			sec += now_time

			if last_bot == 'O':
				last_seco += now_time
			else:
				last_seco = now_time

			last_secb = 0
			Opos  = pos
			last_bot = 'O'
		elif bot == 'B':
			if last_seco > abs( pos - Bpos):
				now_time = 1
			else:
				now_time = abs( pos - Bpos ) - last_seco + 1

			sec += now_time

			if last_bot == 'B':
				last_secb += now_time
			else:
				last_secb = now_time

			last_seco = 0
			Bpos = pos
			last_bot = 'B'
	return sec

		 

def test( data ):
	count = int( data[0] )
	steps = [ (data[i], data[i + 1], )  for i in range(1, count * 2, 2) ]
	return calc_sec(steps)
	

def main():
	lines = file( "ain.txt", "r" ).readlines()
	count = int(lines[0])
	tests = lines[ 1: count+1 ]
	for j, i in enumerate(tests):
		data = [ x.rstrip() for x in i.split( ' ' )]
		print( "Case #%d: %d" % ( j + 1, test( data ) ) )

if __name__ == "__main__": 
	main()
