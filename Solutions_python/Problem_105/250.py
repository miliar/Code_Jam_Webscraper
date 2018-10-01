TYPE = "small"

in_file = open("..\\input\\2012-1C-A-%s.txt" % TYPE, "r")
out_file = open("..\\output\\2012-1C-A-%s.txt" % TYPE, "w")

num_cases = int(in_file.readline().strip())

for case in range(num_cases):  
  answer = "No"
  arrows = {}
  paths = []
  
  N = int(in_file.readline().strip())
  
  for ii in range(1, N + 1):
    arrows[ii] = []
    
  starts = range(1, N + 1)
  ends = range(1, N + 1)
  
  for ii in range(1, N + 1):
    line = in_file.readline().strip()
    for jj in line.split(" ")[1:]:
      arrows[ii].append(int(jj))
      
      if int(jj) in starts:
        starts.remove(int(jj))
        
      if ii in ends:
        ends.remove(ii)
  
  for ii in starts:
    for jj in arrows[ii]:
      paths.append([ii, jj])
      
  while True:
    next_node = 0
    
    for (ii, jj) in paths:
      if jj in arrows:
        next_node = jj
        break
        
    if next_node == 0:
      break
      
    paths_new = [] 
      
    for [ii, jj] in paths:
      if jj == next_node:
        for kk in arrows[jj]:
          if [ii, kk] in paths or [ii, kk] in paths_new:
            answer = "Yes"
            break
          else:
            paths_new.append([ii, kk])
      
      if answer == "Yes":
        break
        
    paths.extend(paths_new)
      
    if answer == "Yes":
      break
        
    del arrows[next_node]
  
  out_file.write("Case #%s: %s\n" % (case + 1, answer))
    
in_file.close()
out_file.close()

print "Done!"