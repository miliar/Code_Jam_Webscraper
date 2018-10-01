from string import maketrans
intab = "abcdefghijklmnopqrstuvwxyz"
outtab = "yhesocvxduiglbkrztnwjpfmaq"
trantab = maketrans (intab, outtab)
l=[]
lines = [line.strip() for line in open('/home/nishchita/Downloads/A-small-attempt2.in')]
n=int(lines[0])
for i in xrange(1,n+1):
  str=lines[i]
  l.append(str.translate(trantab))
j=0
for i in l:
  print "Case #",j+1,":   ", l[j]
  j=j+1