#!/bin/python

def check_min(a, b):
    if a < b:
        return a
    return b

def buy(time, bank, rate, c, f, x):
    time = time
    bank = 0
    rate += f
    return time, bank, rate


def solve(i, line):
    line_t = line.split()
    c, f, x = float(line_t[0]), float(line_t[1]), float(line_t[2])
    #print 'c: ',c,'  f: ',f,'  x: ',x 
    rate = 2
    bank = 0
    min_time = x / rate
    time = float(0)

    while True:
        if bank == c:
            time_no  = time + ((x - bank) / rate)
            time_yes = time + (x / (rate+f))
            if time_no <= time_yes: 
                min_time = time_no
                #print 'time_no'
                break
            else:
                #print 'time_yes'
                time, bank, rate = buy(time, bank, rate, c, f, x)
                #print time, bank, rate
        else:
            if bank <= (c - rate):
                #print bank, time
                time += 1
                bank += rate
            else:
                time+=((c-bank) / rate)
                bank = c

    print "Case #"+str(i+1)+": "+ str(min_time)

      
if __name__ == '__main__':
    n_test = int(raw_input())
    tests = []
    for i in xrange(n_test): 
        tests.extend([raw_input()])
    
    for i in xrange(n_test):
        solve(i, tests[i])