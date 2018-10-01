import sys






ncases = int(sys.stdin.readline())
for i in range(ncases):
  out="Case #%i: "%(i+1)
  arg1=sys.stdin.readline().rstrip('\n').split(' ')
  
  max_shy = int(arg1[0])
  shy_counts = map(int,arg1[1])
  
  invite = 0
  stand = 0
  for shy_level in range(max_shy+1):
    if stand <  shy_level:       # need more people
      invite+=shy_level-stand            # invite
      stand = shy_level
    stand +=shy_counts[shy_level]       # these people will stand up
      
  
  out += str(invite)
  print(out)
  