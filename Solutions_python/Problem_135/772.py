T = int(raw_input())
for t in range(1,T+1):
  print "Case #"+str(t)+":",
  in1 = int(raw_input())
  config1 = [map(int,raw_input().split()) for i in range(4)]
  in2 = int(raw_input())
  config2 = [map(int,raw_input().split()) for i in range(4)]
  s1 = set(config1[in1-1])
  s2 = set(config2[in2-1])
  answer = s1.intersection(s2)
  if len(answer)==0:
    answer="Volunteer cheated!"
  elif len(answer)>1:
    answer="Bad magician!"
  else:
    answer = list(answer)[0]
  print answer
