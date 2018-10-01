'''
Created on 06/05/2011

@author: Julio
'''
class RobotNinja:
  def __init__(self):
    self.pos = 1
    self.orders = []

def separa(case, rb_blue, rb_orange):
  set_blue = True;
  splitted_case = case.split()
  i = 1
  
  for orders in splitted_case:
    if orders == "B":
      set_blue = True
    elif orders == "O":
      set_blue = False
    else:
      if set_blue:
        rb_blue.orders.append((i, int(orders)))
      else:
        rb_orange.orders.append((i, int(orders)))
      i = i + 1
  

def exec_robot(robot, order_number, can_press=True):
  if robot.orders:
    if robot.pos == robot.orders[0][1]:
      if order_number == robot.orders[0][0] and can_press:
        del robot.orders[0]
        
        return True
    else:
      if robot.pos < robot.orders[0][1]:
        robot.pos += 1
      else:
        robot.pos -= 1
  
  return False

def execute(case):
  blue = RobotNinja()
  orange = RobotNinja()
  order = 1
  time = 0
  
  separa(case, blue, orange)
  
  while blue.orders or orange.orders:
    can_press = True
    time += 1
    if exec_robot(blue, order):
      order += 1
      can_press = False
    if exec_robot(orange, order, can_press):
      order += 1
      continue
    
  return time
    


def main():
  input = open("A-large.in", "r")
  output = open("output.txt", "w")
  first_line = True
  i = 1
  
  for line in input:
    if not first_line:
      #print(execute(line.split(' ', 1)[1]))
      output.write("".join(["Case #", str(i), ": ", str(execute(line.split(' ', 1)[1])), "\n"]))
      i += 1
    else:
      first_line = False
    

  
  #case = "O 2 B 1 B 2 O 4"
  #execute(case)
  
  
  output.close()
  input.close()
  

if __name__ == '__main__':
    main()