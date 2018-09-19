
def reverse(x):
    rev = 0
    tmp = x
    tmp2 = x
    tmp2 = (10*(tmp2/10))+1
    while tmp2>0:
      rev*=10
      rev+=tmp%10
      tmp2/=10
      tmp/=10
    return rev

def is_palindrome(x):
  return x == reverse(x)

def main():
  T = int(raw_input())
  for t in xrange(T):
    arr = [int(n) for n in raw_input().split()]
    lo = arr[0]
    hi = arr[1]
    s= 'Case #'+str(t+1)+':'
    print s,
    cnt = 0
    for x in xrange(int(lo**0.5)-2,int(hi**0.5)+2):
      if x*x < lo:
        continue
      if x*x > hi:
        break
      if is_palindrome(x) and is_palindrome(x*x):
        cnt+=1
    print cnt
if __name__=='__main__':
  main()