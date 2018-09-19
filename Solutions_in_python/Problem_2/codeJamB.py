class Time:
	def __init__(self, string):
		[string1, string2] = string.split(" ")
		self.d_hour = int(string1.split(":")[0])
		self.d_min = int(string1.split(":")[1])
		self.a_hour = int(string2.split(":")[0])
		self.a_min = int(string2.split(":")[1])

f_in = open("../Downloads/B-large.in")
N = int(f_in.readline().rstrip())
for test_case in range(N):
	T = int(f_in.readline().rstrip())
	[NA,NB] = (f_in.readline().rstrip().split(" "))
	NA = int(NA)
	NB = int(NB)
	a2b = []
	b2a = []
	for i in range(NA):
		a2b.append(Time(f_in.readline().rstrip()))
	for i in range(NB):
		b2a.append(Time(f_in.readline().rstrip()))
	#print a2b[0].d_hour, a2b[0].d_min, a2b[0].a_hour, a2b[0].a_min
	trains_at_A = 0
	trains_at_B = 0
	trains_needed_at_A = 0
	trains_needed_at_B = 0
	aa = 0
	ad = 0
	ba = 0
	bd = 0
	
	for hour in range(25):
		for min in range(60):
			#Looks for trains that can leave at this time
			arrival_hour = hour
			arrival_min = min-T
			if arrival_min < 0:
				arrival_hour = arrival_hour - 1
				arrival_min = arrival_min + 60
			for t in a2b:
				if t.a_hour == arrival_hour and t.a_min == arrival_min:
					trains_at_B = trains_at_B + 1
					ba = ba + 1
			for t in b2a:
				if t.a_hour == arrival_hour and t.a_min == arrival_min:
					trains_at_A = trains_at_A + 1
					aa = aa + 1

			#Looks for trains that need to leave
			for t in a2b:
				if t.d_hour == hour and t.d_min == min:
					if trains_at_A == 0:
						trains_needed_at_A = trains_needed_at_A + 1
						trains_at_A = 1
					trains_at_A = trains_at_A - 1
					ad = ad + 1

			for t in b2a:
				if (t.d_hour == hour) and (t.d_min == min):
					if trains_at_B == 0:
						trains_needed_at_B = trains_needed_at_B + 1
						trains_at_B = 1
					trains_at_B = trains_at_B - 1
					bd = bd + 1
	#print NA,ad,ba,NB,bd,aa	
	print "Case #%d: %d %d" %(test_case + 1, trains_needed_at_A, trains_needed_at_B)
				
					
	
