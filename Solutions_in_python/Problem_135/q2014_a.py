import io,sys

#qualy 2014-a
def solve(case, r1, s1, r2, s2):
	rows1 = s1.split("\n")[r1-1].split()
	rows2 = s2.split("\n")[r2-1].split()
	result = set(rows1) & set(rows2)
	#print ("#%s & %s = %s", rows1, rows2, result)
	
	if len(result)==0: 
	    print( "Case #{0}: Volunteer cheated!".format(case))
	elif len(result)==1:
		print( "Case #{0}: {1}".format(case, list(result)[0]))
	else: 
		print( "Case #{0}: Bad magician!".format(case))
    
def start(IN):
	for t in range(1, int(IN.readline())+1):
		firstChoose = int(IN.readline())
		firstSet = "".join([IN.readline() for x in range(4)])
		secondChoose= int(IN.readline())
		secondSet = "".join([IN.readline() for x in range(4)])
		solve(t, firstChoose, firstSet, secondChoose, secondSet)
	
start(open(sys.argv[1]))
sys.exit(1)
input = io.StringIO("""3
2
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16
3
1 2 5 4
3 11 6 15
9 10 7 12
13 14 8 16
2
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16
2
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16
2
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16
3
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16""")
start(input)