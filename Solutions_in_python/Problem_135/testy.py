def Determine(List):
    A , B = int(List[0]),int(List[5])
    Ra = set(List[A].split(' '))
    Rb = set(List[B+5].split(' '))
    Int = Ra.intersection(Rb)
    if len(Int)==1:
        return list(Int)[0]
    elif len(Int) == 0:
        return "Volunteer cheated!"
    else:
        return  "Bad magician!"
    
def chunkIt(seq, num):
  avg = len(seq) / float(num)
  out = []
  last = 0.0

  while last < len(seq):
    out.append(seq[int(last):int(last + avg)])
    last += avg

  return out

Out = open('output.in','w')
Output = ''
Case = 0
with open('A-small-attempt1.in','r') as Input:
    Total = Input.read().split('\n')
    Real = Total[1::]
    for i in chunkIt(Real,int(Total[0])):
        Case +=1
        Output += 'Case #%s: %s\n' %(Case,Determine(i))
Out.write(Output)
Out.close()
print Out
        
        
        
