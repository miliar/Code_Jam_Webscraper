# -*- coding: utf-8 -*-
fname = "A-large"
fin = open(fname+".in","r")
fout = open(fname+".out","w")
def gcj_read():
  linestr = fin.readline().strip()
  return [int(numb) for numb in linestr.split()]

numcases = gcj_read()[0]

from collections import defaultdict

wsd = []
for caseno in range(numcases):
    N, M = gcj_read()
    print(N, M)
    journeys = [gcj_read() for _ in range(M)]
    intended_discount = sum(((e-o)*(e-o-1)//2)*p for o,e,p in journeys)
    
    stations = defaultdict(int)
    for o,e,p in journeys:
        stations[o] += p
        stations[e] -= p
    
    stations = sorted(stations.items())
    ticketsfrom = []
    savvy_journeys = []
    
    for stn, p in stations:
        if p == 0:
            continue
        if p > 0:
            #~ print(p, "get on at", stn)
            ticketsfrom.append((stn, p))
            continue
        
        #~ print(p, "get on at", stn)
        # Passengers getting off
        togetoff = -p  # Just easier to think about
        while togetoff > 0:
            origin, tickets = ticketsfrom.pop()
            #~ print("  ", tickets, "from", origin)
            #print(stn, p, origin, tickets)
            if tickets > togetoff:
                used = togetoff
                ticketsfrom.append((origin, tickets-togetoff))
                togetoff = 0
            else:
                used = tickets
                togetoff -= tickets
            #print("->", used)
            savvy_journeys.append((origin, stn, used))
    
    print(ticketsfrom)
    
    #~ for o,e,p in savvy_journeys:
        #~ print(o, "->", e, "(%d)"%p)
    
    savvy_discount = sum(((e-o)*(e-o-1)//2)*p for o,e,p in savvy_journeys)
    
    print(savvy_discount, intended_discount)
    loss = savvy_discount - intended_discount
    outstr = str(loss % 1000002013)
    print("Case #"+str(caseno+1)+": "+ outstr)
    fout.write("Case #"+str(caseno+1)+": "+ outstr +"\n")

fin.close()
fout.close()
