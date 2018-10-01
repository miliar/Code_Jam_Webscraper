# @author Carlos M. Pascal 
# @email cpascal at ac.tuiasi.ro
# Problem D

def genCase(dim):
  return [(x,r,c) for x in range(1, dim+1) for r in range(1, dim+1) for c in range(1, dim+1)]

GABRIEL = 'GABRIEL'
RICHARD = 'RICHARD'  

def classify(x, r, c):
  
  #Rule 0: 
  if x>6:
    print (x, r, c), RICHARD, "R0"
    return RICHARD
  #Rule 1: no solution 
  if (r*c % x) != 0:
    print (x, r, c), RICHARD, "R1"
    return RICHARD
  
  #Rule 2: X>max(R, C)
  if x>max(r,c):
    print (x, r, c), RICHARD, "R1"
    return RICHARD

  #Rule 3: 1-omino | 2-omino - 'GABRIEL' (must be after R1)
  if x<3:
    print (x, r, c),GABRIEL, "R3"
    return GABRIEL
  #Rule 4:  
  if x*2<r*c:
    print (x, r, c), GABRIEL, "R4"
    return GABRIEL
  
  #Rule 5: Exception
  if x==3 and c>1 and r>1:
    print (x, r, c), GABRIEL, "R4"
    return GABRIEL
  
  #Rule 6: Exception 
  print (x, r, c), RICHARD, "R6"
  return RICHARD

"""  
for e in genCase(4):
  (x,r,c) = e
  total+=1
  classify(x,r,c)
"""

def doWork(input, output):
  fin = open(input)
  fout = open(output, 'w')
  no_cases = int(fin.readline())
  no = 1
  for line in fin:
    x, r, c = line.split()
    winner = classify(int(x), int(r), int(c))
    msg = 'Case #{0}: {1}\n'.format(no, winner)
    #print msg
    fout.write(msg)
    no+=1
  fin.close()
  fout.close()

  
input = 'D:\work\codejam2015\prD\inprD.txt'
output = 'D:\work\codejam2015\prD\outprD.txt'
doWork(input, output)


"""  
classify(2, 2, 2)
classify(2, 1, 3)
classify(4, 4, 1)
classify(3, 2, 3)
  
print "Total cases: ", total
print "Classified cases: ", count
"""

    
""" 
def main():
  
if __name__ == '__main__':
  main()
"""
    