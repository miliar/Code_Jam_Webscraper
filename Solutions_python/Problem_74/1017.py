for case in xrange(int(raw_input())):
   
   meh=raw_input().split()
   
   inp=[]
   for i in xrange(int(meh[0])):
      inp.append((meh[1+i*2],int(meh[2+i*2])))
   
   lastpos={'O':1,'B':1}
   lasttime={'O':0,'B':0}
   
   
   time=0
   for i in inp:
      if abs(i[1]-lastpos[i[0]])<=time-lasttime[i[0]]:
         time+=1
      else:
         time+=abs(i[1]-lastpos[i[0]])-(time-lasttime[i[0]])+1
      lasttime[i[0]]=time
      lastpos[i[0]]=i[1]
   
   print "Case #"+str(case+1)+":",time
