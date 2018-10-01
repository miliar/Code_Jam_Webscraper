with open("B-large.in", 'r') as file:
    data = file.read()

lines = data.splitlines()
Ntests = int(lines[0])


for i,line in enumerate(lines[1:]):
  [C,F,X] = [float(n) for n in line.split()]
  N_fab = 0
  N_cookies = 0
  v = 2.0
  
  t_sans = X/v
  t_fab = C/v
  t_cond = C/v + X/(v+F)
  t_total = 0
  
  while t_sans > t_cond:
    t_total += t_fab
    v += F
    t_sans = X/v
    t_fab = C/v
    t_cond = C/v + X/(v+F)
    
  
  t_total += t_sans
  print ''.join(['Case #',str(i+1),':']), t_total

    
  
  
  

  
  
  
  
  
  
  
  
  
  
  
  
