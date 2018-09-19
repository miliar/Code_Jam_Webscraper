import sys

sys.setrecursionlimit(100000)

class TimingList:
	def __init__(self):
		self.times = list()

	def add_time(self,time_to_add):
		self.times.append(time_to_add)

	def eval(self):
		if len(self.times) > 1 and (self.times[len(self.times)-1] > self.times[len(self.times)-2]):
			return self.times[len(self.times)-2]
		else:
			return False

def build_list_item(time_list,rate,time,C,F,X):
	time_to_win = X/rate + time
	time_to_farm = C/rate + time
	rate_after_farm = rate + F

	#print("Time to win: {}\nTime to Farm: {}\nRate after farm: {}\n".format(time_to_win,time_to_farm,rate_after_farm))

	time_list.add_time(time_to_win)
	best_time = time_list.eval()
	if best_time:
		return best_time
	else:
		return build_list_item(time_list,rate_after_farm,time_to_farm,C,F,X)

def gogogo():
	infile = open('input.in','r')
	outfile = open('output.out','w+')

	for test_cases in range(int(infile.readline())):
		inputline = str.split(infile.readline().rstrip('\n'),' ')
		C = float(inputline[0])
		F = float(inputline[1])
		X = float(inputline[2])

		outfile.write("Case #{}: {:0.7f}\n".format((test_cases+1),build_list_item(TimingList(),2.0,0,C,F,X)))

if __name__ == '__main__':
	gogogo()
