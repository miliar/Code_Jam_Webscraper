import sys
import pdb

class node:
  def __init__(self,Value):
    self.color=None
    self.children=[]
    self.value=Value

def get_lines(fDes):
  fDes=open(fDes,'r')
  lines=[]
  for i in fDes.read().split('\n'):
    lines.append(i)
  lines=filter(lambda x:x,lines)
  return lines

def parse_lines(lines):
  map=[]
  for i in lines:
    map.append([node(int(x)) for x in i.split(' ')])
  return map

def get_maps(lines):
  maps=[]
  maps_num=int(lines[0])
  row=1
  for i in range(maps_num):
    height=int(lines[row].split(' ')[0])
    row+=1
    maps.append(parse_lines(lines[row:row+height]))
    row+=height
  return maps

def get_neighbours(map,(row,col)):
  neighbours=[]
  #north
  if row-1>-1:
    neighbours.append((map[row-1][col].value,1))
  #south
  if row+1<len(map):
    neighbours.append((map[row+1][col].value,4))
  #east
  if col+1 < len(map[0]):
    neighbours.append((map[row][col+1].value,3))
  #west
  if col-1>-1:
    neighbours.append((map[row][col-1].value,2))
  return neighbours

def update_map(map,pos,neighbour):
  global global_tag
  if neighbour>4 or neighbour <1:
    print "Coding Error"
    print map
    print pos
    print neighbour
  if neighbour==1:
    target=(pos[0]-1,pos[1])
  if neighbour==2:
    target=(pos[0],pos[1]-1)
  if neighbour==3:
    target=(pos[0],pos[1]+1)
  if neighbour==4:
    target=(pos[0]+1,pos[1])

  if map[pos[0]][pos[1]].color:
    map[target[0]][target[1]].color=map[pos[0]][pos[1]].color
  else:
    if map[target[0]][target[1]].color:
      map[pos[0]][pos[1]].color=map[target[0]][target[1]].color
    else:
      map[target[0]][target[1]].children.append(map[pos[0]][pos[1]])

def update_children(node):
  if node.children==[]:
    return
  for child in node.children:
    child.color=node.color
    update_children(child)

maps=get_maps(get_lines(sys.argv[1]))
counter=0
for map in maps:
  counter+=1
  global_tag=chr(ord('a'))
  for row in range(len(map)):
    for col in range(len(map[0])):
      if (row,col)==(0,0):
        map[row][col].color=global_tag
      #sort neighbours by values
      neighbours=sorted(get_neighbours(map,(row,col)))
      #if it is local maxima
      if neighbours and (map[row][col].value>neighbours[0][0]):
        #we check if we have more than one minimum neighbour
        if len(neighbours)>1:
          if neighbours[0][0]==neighbours[1][0]:
            #we have a tie, we prioorize according to the directions, north>west>east>south
            neighbours=filter(lambda x: neighbours[0][0]==x[0],neighbours)
            nieghbours=[(y,x) for (x,y) in neighbours]
            neighbours=sorted(neighbours)
            update_map(map,(row,col),neighbours[0][1])
            continue
        update_map(map,(row,col),neighbours[0][1])
      else:
        if not map[row][col].color:
          global_tag=chr(ord(global_tag)+1)
          map[row][col].color=global_tag
  for row in map:
    for e in row:
      if e.children!=[]:
        update_children(e) 

counter=0
for map in maps:
  counter+=1
  print "Case #"+str(counter)+":"
  for row in map:
    for e in row:
      print e.color,
    print
