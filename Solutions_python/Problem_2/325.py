#! /usr/bin/python

fd = open("input.in")

num_cases = int(fd.readline())

def sort_timetable(x,y):
  return x[1]-y[1]


for i in range(0, num_cases):
  turnaround = int(fd.readline())
  num = fd.readline()
  (num_a, num_b) = num.split(" ")
  num_a = int(num_a)
  num_b = int(num_b)
  timetable = []
  for j in range(0,num_a):
    t= fd.readline()
    (h1, t, m2) = t.split(":")
    (m1, h2) = t.split(" ")
    timetable.append((0, int(h1)*60 + int(m1), int(h2)*60 + int(m2)))

  for j in range(0,num_b):
    t= fd.readline()
    (h1, t, m2) = t.split(":")
    (m1, h2) = t.split(" ")
    timetable.append((1, int(h1)*60 + int(m1), int(h2)*60 + int(m2)))

  timetable = sorted(timetable, sort_timetable)
#  print turnaround, timetable

  needed = [0, 0]
  available = [0, 0]
  on_road = []

  for j in range(0, len(timetable)):
    cur_time = timetable[j][1]
    for k in range(0, len(on_road)):
#      print cur_time, k, on_road
      if on_road[k][2] == 1 and on_road[k][1] <= cur_time:
        available[on_road[k][0]] += 1
        on_road[k][2] = 2

    if available[timetable[j][0]] > 0:
      available[timetable[j][0]] -= 1
    else:
      needed[timetable[j][0]] += 1
    if (timetable[j][2] + turnaround) < (24*60):
      on_road.append([ 1 - timetable[j][0], timetable[j][2] + turnaround, 1])

  print "Case #%d:" % (i + 1), needed[0], needed[1]
