import sys

def run():
	if len(sys.argv) != 2:
		print "missing file input path"
		return

	path = sys.argv[1]
	f = open(path, "r")
	output = open("output", "w+")

	#first line is T
	tests = f.readline()
	tests = tests.split()
	tests = int(tests[0])
	
	for test in range(tests):
		#keep track of money made
		money = 0
		
		#line1 of test case contains R, k, n
		#R number of runs of roller coaster
		#k number of seats in roller coaster
		#N number of groups
		line1 = f.readline()
		line1 = line1.split()
		runs = int(line1[0])
		seats = int(line1[1])
		groups = int(line1[2])
		
		#list of groups
		line2 = f.readline()
		line2 = line2.split()
		grouplist = [int(i) for i in line2]
		cycle = []
		
		#repeat process for each run
		for run in range(runs):
			seatsremaining = seats
			while grouplist:
				group = grouplist.pop(0)
				if group <= seatsremaining:
			#		print "grouplist"
			#		print grouplist
			#		print "cycle"
			#		print cycle
			#		print "group %d seats remaining %d" % (group, seatsremaining)
					
					seatsremaining = seatsremaining - group
					money = money + group
					cycle.append(group)
					if seatsremaining == 0:
				#		print "!!!!!!!!! 0 SEATS REMAINING !!!!!!!!!!"
						break
				else:
				#	print "grouplist"
			#		print grouplist
			##		print "cycle"
			#		print cycle
		#			print "group %d seats remaining %d" % (group, seatsremaining)
		#			print "!!!!!!!!!! group %d didn't fit !!!!!!!!!!" % group
					grouplist.insert(0, group)
					break
			grouplist.extend(cycle)
	#		print "GROUPLIST RESET"
	#		print grouplist
			cycle = []
			seatsremaining = seats
		#end loop through runs
		output.write("Case #%d: %d\n" % (test+1, money))
	#end loop through tests
	
	f.close()
	output.close()

if __name__ == "__main__":
	run()