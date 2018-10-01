#!/usr/bin/python4
import string
objfile = open('/Users/sandeepsawant/Data/EclipseWorkspace/Code jam/src/A-large.in', 'r')
counter = -1
res = []
for ln in objfile.readlines():
  counter += 1
  if not counter:
    continue
  intTimer = 0
  seq = ln.replace('\n', '').split(' ')
  len_seq = int(seq[0])
  pos = {'O':1,
              'B':1}
  robot_time = {'O':0,
               'B':0}
  first_robo = ''
  first_time = 0
  for j in range(0, len_seq):
    current_rob, perf_step = seq[j * 2 + 1:j * 2 + 3]
    temp_time = (int(perf_step) - pos[current_rob])
    time_elapsed = temp_time * (1 if temp_time > 0 else - 1) + 1
    blnFlag = False
    if first_time and first_robo:
      if first_robo != current_rob:
        difference = (robot_time[current_rob] + time_elapsed) - intTimer
        if difference <= 0:
          intTimer += 1
          blnFlag = True
        else:
          intTimer += difference
      else:
        intTimer += time_elapsed
    else:
      intTimer += time_elapsed
    pos[current_rob] = int(perf_step)
    robot_time[current_rob] += time_elapsed
    if blnFlag:
      robot_time[current_rob] = intTimer
    first_robo = current_rob
    first_time = robot_time[current_rob]
  res.append('Case #%s: %s' % (counter, intTimer))
objfile.close()
objfile = open('A-small-attempt0', 'w')
objfile.write(string.join(res, '\n'))
objfile.close()
f = open('/Users/sandeepsawant/Data/EclipseWorkspace/Code jam/src/test.out', 'w')
f.write(string.join(res, '\n'))
f.close()
