from sys import stdin
read = stdin.readline

ints = lambda:map(int,read().split())
doubles = lambda:map(float,read().split())

def solve():
  row = ints()[0]
  tuples1 = map(tuple,[ints(),ints(),ints(),ints()])
  nums = set(tuples1[row-1])
  rowset = set(nums)
  row = ints()[0]
  tuples2 = map(tuple,[ints(),ints(),ints(),ints()])
  sets = map(set,tuples2)
  #print sets

  
  nums = nums & set(tuples2[row-1])
  candidates = set(tuples2[row-1])
  if not candidates & rowset:
      return "Volunteer cheated!"
  if len(nums) is 1:
    return str(sum(nums))
  else:
    for i in range(4):
      #print sets[i],rowset
      if not len(sets[i] & rowset) is 1:
        return "Bad magician!"
    return "Volunteer cheated!"

for t in range(ints()[0]):
  ans = solve()
  print "Case #%d: %s" % (t+1,ans)