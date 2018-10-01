#!/usr/bin/env python
import math

DEBUG = False

class Events:
  def __init__(self):
    self.event_list = []
    self.event_index = 0
    self.next_event_cache = {}

  def AddEvent(self, robot, button):
    self.event_list.append((robot, button))

  def GetLength(self):
    return len(self.event_list)

  def GetCurrentEvent(self):
    return self.event_list[self.event_index]

  def GetNextEvent(self, robot):
    if self.next_event_cache.has_key(robot):
      index = self.next_event_cache[robot]
      assert(self.event_list[index][0] == robot)
      return self.event_list[index][1]

    for i in range(self.event_index, len(self.event_list)):
      if self.event_list[i][0] == robot:
        self.next_event_cache[robot], index = i, i
        return self.event_list[index][1]
    return None

  def Advance(self):
    self.event_index += 1
    keys = self.next_event_cache.keys()
    for k in keys:
      if self.next_event_cache[k] < self.event_index:
        self.next_event_cache.pop(k)
    return


def OtherRobot(robot):
  return {'O': 'B', 'B': 'O'}[robot]


def MoveTowards(a, b, steps):
  """ Move towards `a` from `b` by `steps` steps."""
  if abs(a-b) <= steps:
    return a
  steps = math.copysign(steps, a-b) # Return steps with the sign of a-b
  return b+steps


def MinimumTimeToCompleteEvents(events):
  time = 0
  position = {'O': 0, 'B': 0}

  for i in range(events.GetLength()):
    debug_position = position.copy() if DEBUG else None

    next_position = {'O': events.GetNextEvent('O'),
        'B': events.GetNextEvent('B')}

    (robot, button) = events.GetCurrentEvent()
    assert(next_position[robot] == button)

    time_required = abs(button - position[robot]) + 1 # To hit the button

    # Update current robot's position
    position[robot] = button

    # Update other robot's position
    other_robot = OtherRobot(robot)
    if next_position[other_robot] is not None:
      position[other_robot] = MoveTowards(next_position[other_robot],
          position[other_robot], time_required)

    if DEBUG:
      print "Time: %3d, CR: (%s, %3d), Other: (%s, %4s), Reqd time: %3d, RO: (%3d -> %3d), RB: (%3d -> %3d)"%(time, 
        robot, button,
        other_robot, next_position[other_robot],
        time_required,
        debug_position['O'], position['O'],
        debug_position['B'], position['B'])
    events.Advance()
    time += time_required

  return time - 1


def ProcessTestCase(test_case):
  events = Events()
  line = raw_input().strip().split()

  for i in range(1, len(line), 2):
    (robot, button) = line[i], int(line[i+1])
    events.AddEvent(robot, button)


  if DEBUG:
    print events.event_list
    print
  time = MinimumTimeToCompleteEvents(events) 
  print "Case #%d: %d"%(test_case+1, time)
  if DEBUG:
    print
  return


def Main():
  test_cases = int(raw_input())
  for t in range(test_cases):
    ProcessTestCase(t)

if __name__ == '__main__':
  Main()

