#!/usr/bin/python

def toMins(time):
  # time = 'HH:MM'
  # return number of minutes after 00:00
  hh, mm = map(int, time.split(':'))
  return 60*hh + mm


def minTrains(AB, BA, T):
  # AB is list of times, [depart, arrive] for trains from A to B
  # BA is time of trains from B to A
  # T is turnaround time in minutes
  A_arrivals   = [t[1] for t in BA]  # times of trains arriving from B
  A_departures = [t[0] for t in AB]  # times of trains leaving A
  
  B_arrivals   = [t[1] for t in AB]
  B_departures = [t[0] for t in BA]
  
  A_arrivals.sort()
  A_departures.sort()
  B_arrivals.sort()
  B_departures.sort()  
    
  # start with infinite number of trains, 
  # try to send only those that are currently in circulation
  
  time = 0
  Astart, Bstart = 0, 0
  Acurrent, Bcurrent = 0, 0
  
  # times for when trains turning around at A will be ready again
  Aturning = [] 
  Bturning = []
  
  events = A_arrivals + A_departures + B_arrivals + B_departures
  
  
  
  while events:
    events.sort()
    
    # get time of next event (arrival or dept at A or B)
    time = events.pop(0)    
        
    # if a train arrives at A, schedule an event in T mins 
    # for when it is ready to go again
    if time in A_arrivals:
      A_arrivals.remove(time)
      events.append(time+T)
      Aturning.append(time+T)
       
    # if a train arrives at B, schedule an event in T mins 
    # for when it is ready to go again
    elif time in B_arrivals:
      B_arrivals.remove(time)
      events.append(time+T)
      Bturning.append(time+T)
      
    elif time in Aturning:
      Aturning.remove(time)
      Acurrent += 1
    
    elif time in Bturning:
      Bturning.remove(time)
      Bcurrent += 1
            
    elif time in A_departures:
      A_departures.remove(time)
      # try to send one of current trains 
      # otherwise increase Astart
      if Acurrent == 0:
        Astart += 1
      else:
        Acurrent -= 1
    
    elif time in B_departures:
      B_departures.remove(time)
      if Bcurrent == 0:
        Bstart += 1
      else:
        Bcurrent -= 1
  
  return (Astart, Bstart)
    

N = int(raw_input())

for i in range(1, N+1):
  AtoB = []
  BtoA = []
  
  t = int(raw_input())
  NA, NB = map(int,(raw_input().split()))
  
  for ii in range(NA):
    AtoB.append(map(toMins, raw_input().split()))
  
  for ii in range(NB):
    BtoA.append(map(toMins, raw_input().split()))
  
  s1, s2 = minTrains(AtoB, BtoA, t)
  print 'Case #%d: %d %d' % (i, s1, s2)

  
  
  
  
  
  

  
  



