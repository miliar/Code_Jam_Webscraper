f = open('Cs0')

def palindrome(x):
  return int(str(x)[::-1]) == x

num_cases = int(f.next())
for T in range(1,num_cases+1):
  line = f.next().strip().split(' ')
  A = int(line[0])
  B = int(line[1])

  sA = int(A**.5-1)
  sB = int(B**.5+1)

  pals = filter(palindrome, range(sA, sB+1))
  squares = map(lambda x: x**2, pals)
  spals = filter(lambda x: palindrome(x) and x >= A and x <= B, squares)

  print "Case #%s: %s" % (T, len(spals))
