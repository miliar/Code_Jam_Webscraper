
def needed_more(S):
  stand = 0
  need_invite = 0
  for i in xrange(len(S)):
    if stand < i and S[i] > 0:
      need_invite += (i - stand)
      stand += need_invite
    stand += S[i] 

  return need_invite

if __name__ == '__main__':
  T = int(raw_input())
  for i in xrange(T):
    S = tuple(int(x) for x in raw_input().split()[1])
    print "Case #%s: %s" % (i+1, needed_more(S))
  
