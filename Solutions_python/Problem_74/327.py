import sys #for argv

def nextMove(moves, robot) :
 # Returns the next button the robot will need to be at; -1 if no further
 #  presses are needed.
 for i in moves : 
  if i[0] == robot :
   return i[1]
 return -1

def getMove(moves, robot, robot_loc) :
 # Uses nextMove to determine the movement of a robot at each point in time.
 # Returns +-1 for direction, 0 for staying still, and 2 for button pressing.
 move = nextMove(moves, robot)
 if move != -1 :
  if move > robot_loc : 
   return 1
  if move < robot_loc :
   return -1
  if move == robot_loc :
   if moves[0][0] == robot :
    return 2
   else :
    return 0
 else :
  return 0

def solve(line,f,caseno) :
 # Solve a line.
 orange_loc = 1
 blue_loc = 1
 words = line.split(" ")
 buttons = int(words[0])
 moves = []
 # Read all the buttons that must be pressed into moves[]
 for i in range(buttons) :
  robot = words[2*i+1]
  button = int(words[2*i+2])
  moves.append((robot,button))
 ct = 0
 while len(moves) > 0 :
  # Get the moves each must make, then increment the moves counter.
  mv = (getMove(moves,'O',orange_loc), getMove(moves,'B',blue_loc))
  if mv[0] == 2 : 
   moves = moves[1:]
   print ("Orange: press button %d"%orange_loc),
  else : 
   orange_loc += mv[0]
   print ("Orange: move to %d"%orange_loc)
  if mv[1] == 2 : 
   moves = moves[1:]
   print ("Blue: press button %d"%blue_loc)
  else :
   blue_loc += mv[1]
   print ("Blue: move to %d"%blue_loc)
  ct += 1
 # Now write the answer.
 f.write("Case #%d: %d\n"%(caseno,ct))
  
# Read in both filenames from argv, then load the input, split it by lines, and 
#  feed it, line by line, into solve().
filename = sys.argv[1]
f = open(filename)
inpt = f.read()
f.close()
inpt_lines = inpt.split("\n")
cases = int(inpt_lines[0])
f = open(sys.argv[2],"w")
caseno = 1
for i in inpt_lines[1:1+cases] :
 solve(i,f,caseno)
 caseno += 1
f.close()
