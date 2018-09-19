import csv

def reverse_int(n):
  m = 0
  while n > 0:
    m = 10*m + n%10
    n /= 10
  return m

if __name__ == "__main__":

  limit = 100000000000000
  fas = []
  for n in xrange(1,int(limit**0.5)+1):
    if n == reverse_int(n):
      m = n**2
      if m == reverse_int(m):
        fas.append(m)


  f = csv.reader(open('C-large-1.in','r'), delimiter = ' ')
  out = open("C-large-1-2.out","w")

  T = int(f.next()[0])

  for case in xrange(1,T+1):
    [A, B] = [int(x) for x in f.next()]
    count = 0
    for n in fas:
      if n >= A and n <= B:
        count += 1
    out.write("Case #%d: %d\n" % (case,count))

  out.close()
