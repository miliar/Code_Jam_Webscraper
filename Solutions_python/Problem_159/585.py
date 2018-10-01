def read_int():return int(raw_input())
def read_intarray():return map(int,raw_input().split())

def case1(l):
  res = 0
  for i in xrange(len(l)-1):
    if l[i] > l[i+1]:
      res += l[i]-l[i+1]
  return res
  
def case2(l):
  rate = 0
  for i in xrange(len(l)-1):
    if l[i]>l[i+1]:
      rate = max(rate,l[i]-l[i+1])
  res = 0
  for i in xrange(len(l)-1):
    if l[i]-rate < 0:
      curr = l[i]
    else:
      curr = rate
    res += curr
  return res
def main():
    T = read_int()
    for i in xrange(T):
	n = read_int()
        l = read_intarray()
        print "Case #"+str(i+1)+": " + str(case1(l))+" "+str(case2(l))

if __name__ == '__main__':
    main()