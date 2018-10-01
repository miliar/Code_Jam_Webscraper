for t in xrange(int(raw_input())):
  _trash = raw_input()
  a = map(float, raw_input().split())
  b = map(float, raw_input().split())
  a.sort()
  b.sort()
  #print
  #print a
  #print b
  # Honest solution
  b_pointer = 0
  honest_score = 0
  for a_pointer in xrange(len(a)):
    while b_pointer < len(b) and b[b_pointer] < a[a_pointer]:
      b_pointer += 1
    if b_pointer >= len(b):
      honest_score = len(a) - a_pointer 
      break
    b_pointer += 1

  #Lying solution
  b_pointer = len(b) - 1
  a_pointer = len(a) - 1
  lying_score = 0
  while a_pointer < len(a) and b_pointer >= 0:
    while b_pointer >= 0 and a[a_pointer] < b[b_pointer]:
      b_pointer -= 1
    if b_pointer < 0:
      break
    a_pointer -= 1
    b_pointer -= 1
    lying_score += 1
    
  print "Case #" + str(t + 1) + ":", lying_score, honest_score
