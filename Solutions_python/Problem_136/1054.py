from __future__ import division
f=open('B-large.in')
g=open('Result.in','w')
T=int(f.readline())
for i in range(T):
    C,F,X=map(float,f.readline().split())
    rate_of_cookies=2
    elapsed_time=0
    while X/rate_of_cookies>C/rate_of_cookies+X/(rate_of_cookies+F):
        elapsed_time+=C/rate_of_cookies
        rate_of_cookies+=F
    elapsed_time+=X/rate_of_cookies
    g.write('Case #'+str(i+1)+': '+str(elapsed_time)+'\n')
g.close()
f.close()
