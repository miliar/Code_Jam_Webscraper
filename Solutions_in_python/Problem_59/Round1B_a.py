'''
Created on 22.05.2010

@author: shelajev
'''

filename = 'A-large'
#filename = 'B-sample'

if __name__ == '__main__':
  with open(filename + '.in') as file:
    out = open(filename + '.out', 'w')
    C = int(file.readline());
    for i in range(1, C + 1):
      r = 0
      all = set()
      toadd = []
      line = file.readline().strip().split(' ')
      N = int(line[0])
      M = int(line[1])
      for j in range(N):
        line = file.readline().strip()
        all.add(line[1:])
      for j in range(M):
        line = file.readline().strip()
        toadd.append(line[1:])
      toadd.sort();
      for e in toadd:
        d = 0
        while((e not in all) and (e != '')):
#          print(e)
          all.add(e)
          idx = e.rfind('/')
          if(idx == -1):
            d = d + 1
            break
          e = e[0:idx]
          d = d + 1
          
        r = r + d  
      
      z = 'Case #{0}: {1}\n'.format(i, r)
      out.write(z)
      print(z)