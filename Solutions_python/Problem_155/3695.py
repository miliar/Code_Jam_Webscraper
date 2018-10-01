num_cases = int(raw_input())

for case in range(num_cases):
  size, n = str.split(raw_input())
  sum = 0
  invitations = 0
  for i, digit in enumerate(n):
    digit = int(digit)
    if i > sum and digit > 0:
      invitations += i - sum
      sum += invitations
    sum += digit
  print "Case #"+ str(case+1) +":", invitations
