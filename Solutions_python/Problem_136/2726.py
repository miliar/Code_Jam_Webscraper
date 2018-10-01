'''
Created on Apr 12, 2014

@author: Yuan
'''

if __name__ == '__main__':
    t = int(raw_input())
    for i in range(t):
        c,f,x = tuple([float(x) for x in raw_input().split(" ")])
        ans = 0.0
        curr = 2.0
        acc = 0.0
        while True:       
            if (x-acc)/curr > x/(curr+f) + (c-acc)/curr:
                ans += (c-acc)/curr
                acc = 0
                curr += f
            else:
                ans += (x-acc)/curr
                acc = x                
                break
        print "Case #%d: %.7f" % ((i+1),ans)
                