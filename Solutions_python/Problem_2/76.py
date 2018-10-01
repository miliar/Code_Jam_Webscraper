

def time_to_min(time_str):
	parts=time_str.split(':')
	return int(parts[0])*60+int(parts[1])


def parseOneEntry(input_f,from_where,to_where,turnaround_time):
	parts=input_f.readline().split()
	l_time=time_to_min(parts[0])
	a_time=time_to_min(parts[1])
	return [[l_time,'1L',from_where,parts[0]],[a_time+turnaround_time,'0R',to_where,parts[1]]]

def parseTimetable(input_f,turnaround_time):
	parts=input_f.readline().split()
	FromA=int(parts[0])
	FromB=int(parts[1])
	
	events=[]
	for i in range(FromA):
		entry_events=parseOneEntry(input_f,'A','B',turnaround_time)
		events.extend(entry_events)
		
	for i in range(FromB):
		entry_events=parseOneEntry(input_f,'B','A',turnaround_time)
		events.extend(entry_events)
	
	return events


def howmany(input_f):
	turnaround_time=int(input_f.readline())
	events=parseTimetable(input_f,turnaround_time)
	
	events.sort()
	
	ready_trains={'A':0,'B':0}
	added_trains={'A':0,'B':0}
	
	for next in events:
		where=next[2]
		if next[1]=='1L':
			if ready_trains[where]==0:
				added_trains[where]+=1
				ready_trains[where]+=1
			ready_trains[where]-=1
		else:
			ready_trains[where]+=1		

	return added_trains['A'],added_trains['B']
	
def main_solve():
	import sys
	
	#sys.stdout=open("debug.output","w")
	
	input_f=open(sys.argv[1],"r")
	first_line=input_f.readline()
	case_num=int(first_line)
	result_f=open("result.output","w")
	
	for i in range(case_num):
		result_f.write("Case #%d: "%(i+1))
		
		an,bn=howmany(input_f)
		result_f.write("%d %d\n"%(an,bn))
		i+=1
	
	
main_solve()