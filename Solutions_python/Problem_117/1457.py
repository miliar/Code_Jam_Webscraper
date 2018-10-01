def Lawnmower(filename):
         fob = open(filename,'r')
         out = open('/home/hussein/Programming/a.out','w')
         for tc in xrange(1,int(fob.next().rstrip('\r\n'))+1):
                  deslawn=[]
                  lawn=[]
                  s = fob.next().rstrip('\r\n').split()
                  n = int(s[0])
                  m = int(s[1])
                  for i in range(n):
                           temp=fob.next().rstrip('\r\n').split()
                           temp=[int(x) for x in temp]
                           deslawn.append(temp)
                  lawn=[[100]*m for x in range(n)]

                  #each row edge
                  for i in range(n):
                           mx = max(deslawn[i])
                           lawn[i] = [mx for x in range(m)]
                  #each col edge
                  translawn = [list(i) for i in zip(*lawn)]
                  transdes = [list(i) for i in zip(*deslawn)]
                  for i in range(m):
			   if not all(a==b for a, b in zip(translawn[i], transdes[i])):
				   mx = max(transdes[i])
				   translawn[i] = [mx for x in range(n)]
                  lawn = [list(i) for i in zip(*translawn)]
                  deslawn = [list(i) for i in zip(*transdes)]
                  if all(i==j for i, j in zip(lawn, deslawn)):
                           case='YES'
                  else:
                           case='NO'

                  out.write('Case #%d: %s\n' % (tc,case))
         fob.close()
         out.close()
                           
                           
                           
                           
                           
                  
