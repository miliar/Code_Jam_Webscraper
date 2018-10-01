f=open('A-small-attempt0.in')
d=open('A-small-attempt0.out','a')
cases = int(f.readline())
i=0
def s(a):
  return [int(x) for x in a.readline().split()]

while 1:
  r1=0;o=[];i+=1
  try:
    r1=int(f.readline())
    a1=[s(f),s(f),s(f),s(f)]
    r2=int(f.readline())
    a2=[s(f),s(f),s(f),s(f)]
  except:
    break
  for x in a1[r1-1]:
    if x in a2[r2-1]:
      o.append(x)
  if len(o) is 1:
    #print(o[0])
    d.write('Case #'+str(i)+': '+str(o[0])+'\n')
  elif len(o) > 1:
    #print('Bad magician!')
    d.write('Case #'+str(i)+': Bad magician!\n')
  else:
    #print('Volunteer cheated!')
    d.write('Case #'+str(i)+': Volunteer cheated!\n')
    
d.close()
