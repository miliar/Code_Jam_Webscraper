palindrome=lambda x: int(str(x)[::-1])
is_palindrome= lambda x: str(x)==str(x)[::-1]
square=lambda x: int((x**.5))**2
sqrt=lambda x: int(x**.5)
is_square=lambda x: square(x)==x
fair_and_square=lambda x: is_square(x) and is_palindrome(x) and is_palindrome(sqrt(x))

for case in xrange(int(raw_input())):
  a,b=map(int,raw_input().split())
  print 'Case #%d: %d'%(case+1, len([(i,square(i)) for i in xrange(a,b+1) if fair_and_square(i)]))
