with open("D-small-attempt0.in") as f:
  num_cases = int(f.readline().strip())
  for case in range(1,num_cases+1):
    data = [int(d) for d in f.readline().split()]
    X = data[0]
    R = data[1]
    C = data[2]
    
    if X >= 7:
      answer = "RICHARD"
    elif (R*C)%X != 0:
      answer = "RICHARD"
    elif R >= X and C >= X:
      answer = "GABRIEL"
    elif R < X and C < X:
      answer = "RICHARD"
    elif X<=2:
      answer = "GABRIEL"
    elif X==3:
      if R==1 or C==1:
        answer = "RICHARD"
      else:
        answer = "GABRIEL"
    elif X==4:
      if R<=2 or C<=2:
        answer = "RICHARD"
      else:
        answer = "GABRIEL"
    elif X==5:
      if R<=2 or C<=2:
        answer = "RICHARD"
      else:
        answer = "GABRIEL"
    else:
      if R<=3 or C<=3:
        answer = "RICHARD"
      else:
        answer = "GABRIEL"
        
    print("Case #{}: {}".format(case, answer))