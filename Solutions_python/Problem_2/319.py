#!/usr/local/bin/python

def convert_time(t):
  h, m = map(int, t.split(':'))
  return h*60 + m

A = 0
B = 1

def incA(s): s[A] += 1
def incB(s): s[B] += 1
def decA(s): s[A] -= 1
def decB(s): s[B] -= 1

arriveA = (0, incA)
arriveB = (1, incB)
leaveA = (2, decA)
leaveB = (3, decB)

N = int(raw_input())
for i in range(1, N+1):
  print "Case #%d:" % i,

  T = int(raw_input())
  NA, NB = map(int, raw_input().split())

  deficit = [0, 0]
  stations = [0, 0]
  schedule = []

  for j in range(NA):
    times = raw_input().split()
    start, finish = tuple(map(convert_time, times))
    schedule += [(start, leaveA), (finish+T, arriveB)]

  for j in range(NB):
    times = raw_input().split()
    start, finish = tuple(map(convert_time, times))
    schedule += [(start, leaveB), (finish+T, arriveA)]

  schedule.sort()
  #print schedule

  for (t, (n, action)) in schedule:
    action(stations)
    deficit[A] = min(deficit[A], stations[A])
    deficit[B] = min(deficit[B], stations[B])

  print -deficit[A], -deficit[B]


