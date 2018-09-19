
mem = {}

#def decompose(n1,n2):
#  cpt = 0
#  if n1 < n2:
#    cpt += decompose(n1*2,n2)
#  else:
#    return 1 + cpt
#  return cpt
 
def decompose(nb1,nb2):
  cpt = 0
  while(nb1<nb2):
    cpt += 1
    nb1 *= 2
  return cpt

def is_power2(num):
  return num != 0 and ((num & (num-1)) == 0)

nb_cases = int(raw_input())

for i in xrange(nb_cases):
  fract = raw_input().split('/')
  if is_power2(int(fract[1])) == False:
    print("Case #%d: impossible" % (i+1))
  else:
    print("Case #%d: %d" % (i+1,decompose(int(fract[0]),int(fract[1]))))
