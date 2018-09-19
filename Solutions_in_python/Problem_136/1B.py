import sys
import math

def time(farms, cookies, F):
	rate = float(farms * F)
	return float(cookies) / float(rate + 2)

def main():
  inputfile = open(sys.argv[1])
  T = int(inputfile.readline().rstrip())

  for case in range(1, T + 1):
    # rate = 2.0
    # nfarms = 1.0
    [C, F, X] = [float(i) for i in inputfile.readline().rstrip().split(" ")]
    # print str(time(0, X, F))
    # costs = []
    # rates = [2 + (F * nfarms) for nfarms in range(0, 2)]
    # costs = [C/rate for rate in rates]

    # # time to build each farm
    # totes = []
    # # print costs
    # # print

    # for c in range(0, len(costs)):
    # 	if c is 0:
    # 		totes.append(costs[0])
    # 	else:
	   #  	totes.append( (totes[c - 1] + costs[c]) )
    # # print rates
    # # while

    # min_time = X/2.0

    # # for n in range(2, int(math.ceil(X))):
    # 	# min_time = min(min_time, (X/rates[n]) + totes[n - 1 if n > 0 else n])
    # old_time = X/2.0
    # n = 0.0
    # new_time = (X/(rates[1])) + totes[1]

    # last_farm_time = C/2.0

    # old_old_time = old_time

    # while old_time > new_time:
    # 	old_old_time = old_time
    # 	old_time = new_time
    # 	n = n + 1.0
    # 	new_time = (X/(2.0 + (F*n))) + last_farm_time
    # 	last_farm_time = last_farm_time + (C/(2.0 + (F*n)))

    n = 0.0
    time = 0.0
    while (X/(2.0 + F*n)) > (X/(2.0 + F*(n+1)) + C/(2.0 + F*n)):
    	time = time + (C/(2.0 + F*n))
    	n = n + 1.0

    time = time + X/(2.0 + F*n)

    # print 'Case #' + str(case) + ': ' + str(min_time)
    print 'Case #' + str(case) + ': ' + "%0.7f" % time
    # print totes
    # return
    

  return

if __name__ == '__main__':
  main()