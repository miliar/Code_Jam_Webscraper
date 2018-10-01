##import ???

def main():

  def squeez(n, k):
    l2k = 0
    k2 = k
    while k2 > 1:
      k2 //= 2
      l2k += 1
    papapa = [[n, 1]]
    for i in range(l2k):
      subpa = []
      for j in range(len(papapa)): papapa[j][0] -= 1
      for j in papapa:
        potmin = j[0] // 2
        potmax = j[0] - potmin
        if [potmax,0] not in subpa: subpa.append([potmax,0])
        if [potmin,0] not in subpa: subpa.append([potmin,0])
      for j in papapa:
        potmin = j[0] // 2
        potmax = j[0] - potmin
        for l in range(len(subpa)):
          if subpa[l][0] == potmax: subpa[l][1] += j[1]
          if subpa[l][0] == potmin: subpa[l][1] += j[1]
      papapa = subpa
    num = papapa[1][0] - 1 if k + 1 - 2**l2k > papapa[0][1] else papapa[0][0] - 1
    return [num - num // 2, num // 2]

  ##f1=open(r'C:\Users\mumin\Documents\gcj\testfile.in','r')
  ##f2=open(r'C:\Users\mumin\Documents\gcj\testfile.out','w')
  ##f1=open(r'C:\Users\mumin\Documents\gcj\C-small-1-attempt1.in','r')
  ##f2=open(r'C:\Users\mumin\Documents\gcj\C-small-1-attempt1.out','w')
  ##f1=open(r'C:\Users\mumin\Documents\gcj\C-small-2-attempt0.in','r')
  ##f2=open(r'C:\Users\mumin\Documents\gcj\C-small-2-attempt0.out','w')
  f1=open(r'C:\Users\mumin\Documents\gcj\C-large.in','r')
  f2=open(r'C:\Users\mumin\Documents\gcj\C-large.out','w')
  f1.readline()
  linenum = 0
  for line in f1:
    if not line: continue
    linenum += 1
    ind = line.find(' ')
    n = int(line[:ind])
    k = int(line[ind + 1:-1])
    f2.write('Case #{}: {}\n'.format(linenum, ' '.join([str(i) for i in squeez(n, k)])))
  f1.close()
  f2.close()  

if __name__ == '__main__':
  main()