
fo=open("A-small-attempt0.in", "r")


t=int(fo.readline())

for c in xrange(1,t+1):
   g = {}
   for i in xrange(1,17):
      g[str(i)]=0

   q1ans=fo.readline()
   ln=[]
   for i in xrange(0,4):
      ln.append(fo.readline().split())

   for e in ln[int(q1ans)-1]:
      g[str(e)]+=1

#   print g

   q2ans=fo.readline()
   ln=[]
   for i in xrange(0,4):
      ln.append(fo.readline().split())

   for e in ln[int(q2ans)-1]:
      g[str(e)]+=1

#   print g

   ans_gk=max(g,key=g.get)
   ans_gv=sorted(g.values())

   if 2 in g.itervalues():
      if ans_gv[-2] == 2:
         print 'Case #%s: Bad magician!' % (c)
      elif max(ans_gv) == 2:
         print 'Case #%s: %s' % (c, ans_gk)

   if max(ans_gv) < 2:
      print 'Case #%s: Volunteer cheated!' % (c)

#   print g
#   print sorted(g.values())
