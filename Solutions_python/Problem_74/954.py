#!/usr/bin/python -O

import sys

def main(argv=None):

  if argv is None:
    argv = sys.argv

  try: 
    f = open(sys.argv[1], 'r')
  except IndexError as e:
    print "Please specify an input file"
    return 127
  except IOError as e:
    print "Could not read file!"
    return 127

  n = int(f.readline())
  n_case = 1
  buttons = 0
  time = 0
  ORANGE = 'O'
  BLUE = 'B'
  while n_case <= n:
    line = f.readline().split()
    c = line[1:]
    #[5,8]
    orange = [int(c[x+1]) for x in range(len(c)) if c[x] == 'O' ]
    #[100]
    blue = [int(c[x+1]) for x in range(len(c)) if c[x] == 'B' ]

    o_aux = orange[:]
    b_aux = blue[:]

    o_aux.reverse() 
    b_aux.reverse() 

    #n_case += 1
    #continue

    if len(o_aux) > 0:
      nextO = o_aux.pop()

    if len(b_aux) > 0:
      nextB = b_aux.pop()

    #[('O',5),('O',8),('B',100)]
    tuplist = []
    for k in range(0,len(c),2):
      tuplist.append((c[k],int(c[k+1])))
    #print tuplist

    pushed_button = False
    robot_pos = {ORANGE:1, BLUE:1}
    #print robot_pos

    for color,button_position in tuplist:
      while not pushed_button:
        if robot_pos[color] < button_position:
          robot_pos[color] = robot_pos[color] + 1 
        elif robot_pos[color] > button_position:
          robot_pos[color] = robot_pos[color] - 1 
        else:
          pushed_button = True
          if color == ORANGE:
            if len(o_aux) > 0:
              nextO = o_aux.pop()
          else:
            if len(b_aux) > 0:
              nextB = b_aux.pop()
           
        if color == ORANGE:
          if len(blue) > 0 and nextB > robot_pos[BLUE]:
            robot_pos[BLUE] = robot_pos[BLUE] + 1
          elif len(blue) and nextB < robot_pos[BLUE]:
            robot_pos[BLUE] = robot_pos[BLUE] - 1
        else:
          if len(orange) > 0 and nextO > robot_pos[ORANGE]:
            robot_pos[ORANGE] = robot_pos[ORANGE] + 1
          elif len(orange) > 0 and nextO < robot_pos[ORANGE]:
            robot_pos[ORANGE] = robot_pos[ORANGE] - 1
        time = time + 1
      pushed_button = False
    print "Case #" + str(n_case) + ': ' + str(time)
    n_case += 1
    time = 0
  f.close()
  return 0

if __name__ == "__main__":
    sys.exit(main())
