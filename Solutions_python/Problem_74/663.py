#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys

def next_button(type, cur, buttons):
  for i in range(cur, len(buttons)):
    if buttons[i][0] == type:
      return buttons[i]
  return None    # nothing to do

case = int(sys.stdin.readline())
for c in range(0, case):
  data = sys.stdin.readline().strip().split(' ')
  (num, data) = (data[0], data[1:])
  buttons = [(item[0], int(item[1])) for item in zip(data[0::2], data[1::2])]

  cur = 0
  (blue_pos, orange_pos) = (1, 1)
  next_blue = next_button('B', cur, buttons)
  next_orange = next_button('O', cur, buttons)

  turn = 0
  while next_blue or next_orange:
    # print '-------Turn: %s------------' % turn
    cur_button = buttons[cur]
    # print cur, cur_button
    # print '  B %s, %s' % (blue_pos, next_blue)
    # print '  O %s, %s' % (orange_pos, next_orange)
    
    (blue_moved, orange_moved) = (False, False)
    if next_blue and next_blue[1] != blue_pos:
      blue_pos += (1 if next_blue[1] > blue_pos else -1)
      blue_moved = True
    if next_orange and next_orange[1] != orange_pos:
      orange_pos += (1 if next_orange[1] > orange_pos else -1)
      orange_moved = True

    if cur_button[0] == 'O' and not orange_moved \
           and next_orange and next_orange[1] == orange_pos:
      cur += 1
      next_orange = next_button('O', cur, buttons)
      # print 'Push Orange'
    elif cur_button[0] == 'B' and not blue_moved \
             and next_blue and next_blue[1] == blue_pos:
      cur += 1
      next_blue = next_button('B', cur, buttons)
      # print 'Push Blue'
    turn += 1
    # print cur, cur_button
    # print '  B %s, %s' % (blue_pos, next_blue)
    # print '  O %s, %s' % (orange_pos, next_orange)
  
  ans = turn
  print "Case #%d: %d" % (c+1, ans)
