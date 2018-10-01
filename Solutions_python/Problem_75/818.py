import os

input = open('B-large.in', 'r')
output = open('B-large.out', 'w')


def formatted_list(listy):
    lenny = len(listy)
    count = 1
    stringy = "["
    for l in listy:
        stringy += l
        if count < lenny:
            stringy+=", "
        count += 1
    stringy += "]"
    return stringy
    
def solve_me(c_list, o_list, spell):
  output_list = []
  cl = len(c_list)
  ol = len(o_list)
  for s in spell:
      output_list.append(s)
      # check output_list for combos
      l = len(output_list)
      if l > 1 and cl > 0:
          a = output_list[l-1] # last element
          b = output_list[l-2] # second to last element
          for c in c_list:
              if (a == c[0] and b == c[1]) or (a == c[1] and b == c[0]):
                  # delete both and create new entry
                  del(output_list[l-1])
                  del(output_list[l-2])
                  output_list.append(c[2])
      l = len(output_list)
      if l > 1 and ol > 0:
          for o in o_list:
              if o[0] in output_list and o[1] in output_list:
              # what if d[0] and d[1] are the same?
              # element cant be opposed to itself, so scratch that...
                  del(output_list[:])
                      
  
  return formatted_list(output_list)

T = int(input.readline()) # Number of Test cases
c_list = []
o_list = []
for t in xrange(T):
    # parse test case data
    input_line = input.readline()
    input_list = input_line.split()
    C = int(input_list[0])
    c_list = input_list[1:C+1]
    D = int(input_list[C+1])
    o_list = input_list[C+2:C+2+D]
    spell = input_list[C+D+3]
    answer = solve_me(c_list, o_list, spell)
    output.write("Case #%d: %s"%(t+1, answer) + os.linesep)
    
output.close()
input.close()
