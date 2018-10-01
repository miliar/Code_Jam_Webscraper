__author__ = 'rcarino'
import sys

def min_cookies(c, f, x):
    rate = 2.0
    secs = 0.0
    cookies = 0.0
    while cookies < x:
        # farm or wait
        ttf = c/rate # Time to buy farm
        farm_time = secs + ttf + x/(rate+f) # time to X after buying farm
        no_farm_time = secs + x/rate # time to X w/o buying farm
        if farm_time < no_farm_time:
            secs += ttf
            rate += f
        else:
            return no_farm_time

with open(sys.argv[1]) as f:
# with open('cookies_simple') as f:
    contents = f.readlines()
    for i in range(int(contents.pop(0))):
        c, f, x = [float(f) for f in contents.pop(0).split(' ')]
        print 'Case #{0}: {1}'.format(i+1, min_cookies(c, f, x))