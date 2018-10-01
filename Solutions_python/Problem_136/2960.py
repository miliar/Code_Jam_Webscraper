
def farm_gen(F, C):
  last = C/2.0
  yield last
  i = 1
  while True:
    last += C/(2.0+i*F)
    yield last
    i += 1



def T(n, t, F, f_gen): 

  if n == 0:
    return t/2.0

  s = f_gen.next()
  return s + t/(2.0 + n*F)


a = input()

b = open("file1", 'w')

for i in xrange(a):

  C, F, X = map(float,raw_input().split(' '))

  g = farm_gen(F, C)

  min_t = T(0, X, F, g)

  j = 1
  while True:

    current = T(j, X, F, g)

    if current < min_t:
      min_t = current
      j += 1

    else:
      b.write("Case #%d: %.7f\n" % (i+1, min_t))
      break
b.close()