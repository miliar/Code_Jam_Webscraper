def isP(st):
         if len(st)<1:
                  return True
         else:
                  if st[0] == st[-1]:
                           return isP(st[1:-1])
                  else:
                           return False
