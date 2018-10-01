#
#Input
#
#The first line of the input gives the number of test cases, T. 
#T test cases follow. Each consists of one line with a string S 
#and an integer K. S represents the row of pancakes: each of 
#its characters is either + (which represents a pancake that is
# initially happy side up) or - (which represents a pancake 
#that is initially blank side up).
#
#Output
#
#For each test case, output one line containing Case #x: y, 
#where x is the test case number (starting from 1) and y is 
#either IMPOSSIBLE if there is no way to get all the pancakes 
#happy side up, or an integer representing the the minimum 
#number of times you will need to use the oversized pancake 
#flipper to do it.
#
# Limits
# 1 <= T <= 100.
# Every character in S is either + or -.
# 2 <= K <= length of S.
# Small dataset
# 2 <= length of S <= 10.
# Large dataset
# 2 <= length of S <= 1000.
# 1 <= N <= 10**18.


# 3
# ---+-++- 3
# +++++ 4
# -+-+- 4
#
# Case #1: 3
# Case #2: 0
# Case #3: IMPOSSIBLE


#
# A set of 5 threads 
#  A queue of jobs (test cases)
#  An array of results
# once Queue is empty 
#	print results

from Queue import Queue
from Queue import PriorityQueue
from threading import Thread
import time

#Globals
num_of_threads = 5
jobs_queue = Queue()
results_queue = PriorityQueue(maxsize=100)

class Job:
	""" Simple class for jobs """
	cakes = []
	k = 0
	test = 0

	def __init__(self, test, cakes, k):
		self.test = test
		self.cakes = cakes
		self.k = k

class Result:
	""" Simple class for results """
	test = 0
	flips = 0

	def __init__(self, test, flips):
		self.test = test
		self.flips = flips

def problem( T ):

	# set the workers
	for it in range(num_of_threads):
		worker = Thread(target=do_job, args=(it, jobs_queue, results_queue))
		worker.setDaemon(True)
		worker.start()

	# set the jobs (consume items)
	case = 0
	while ( T > 0 ):
		case = case + 1
		T = T - 1
		inp = raw_input()
		cakes, k = inp.split(' ')
		arr_cakes = []
		for c in cakes:
			if c == '-':
				arr_cakes.append(1)
			else: # +
				arr_cakes.append(0)
		job = Job(case, arr_cakes, int(k) ) 
		jobs_queue.put(job)

	#wait for jobs completed
	jobs_queue.join()
	# following step is print results
	print_jobs_results()

def do_job(thread_num, thread_q, thread_res):
	"""
	Note that this workers ends when the 
	Main thread ends
	"""
	while ( True ):
		job = thread_q.get()
		#print " t %d working on test %d" % (thread_num, job.test)
		flips = count_flips(job.cakes, job.k)
		res = Result(job.test, flips if flips >= 0 else "IMPOSSIBLE")
		thread_res.put( (job.test, res) )
		jobs_queue.task_done()

def print_jobs_results():
	while( not results_queue.empty() ):
		result = results_queue.get()
		print "Case #%s: %s" % ( result[1].test, result[1].flips )

def count_flips( cakes, k ):	
	length = len(cakes)
	count = 0
	
	for curr in range(length):
		if ( cakes[curr] == 1 ):
			#flip the k (curr + next)
			if ( (length - curr) >= k ):
				count += 1
				for i in range(k):
					cakes[curr + i] = flip(cakes[curr + i])
			else:
				# Is not possible
				return -1
		#else means it is + (0)
	return count

def flip(value):
	return (value + 1) % 2


if __name__ == '__main__':
	T = int(raw_input())
	problem(T)
	
 