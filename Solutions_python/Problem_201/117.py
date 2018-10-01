
from queue import Queue

def solve(n,k):
  if 4*k > 3*n+5:
    temp = 1
  else:
    temp = Planner(n,k).solve()
  smaller = (temp-1)//2
  return (temp-smaller-1,smaller)

class Planner:
  def __init__(self,n,k):
    self.q=Queue()
    self.k=k
    
    # Buffer before adding things to the queue
    self.b_sum = 1
    self.b_size = n

  def solve(self):
    while self.k > 0:
      size=self.iterate()
    return size
    
  def iterate(self):
    mult,size=self.get()
    if size & 1:   # size is odd
      self.put(2*mult,size//2)
    else:
      self.put(mult,size//2)
      self.put(mult,size//2-1)
    self.k-=mult
    return size

  def put(self,mult,size):
    if self.b_size == -1:
      self.b_sum = mult
      self.b_size = size
    elif size == self.b_size:
      self.b_sum+=mult
    elif size < self.b_size:
      self.q.put((self.b_sum,self.b_size))
      self.b_sum = mult
      self.b_size = size
    else:
      raise Exception ("size = " +str(size)
                       +" should not be larger than b_size "+str(self.b_size))
                       
      
  def get(self):
    if self.q.empty():
      assert self.b_size != -1
      temp = (self.b_sum,self.b_size)
      self.b_size = -1
      return temp
    else:
      return self.q.get()
  



if __name__ == "__main__":
  t = int(input())
  for i in range(1, t + 1):
    n,k= [int(s) for s in input().split(" ")]
    big,small = solve(n,k)
    print("Case #{}: {} {}".format(i, big, small))




