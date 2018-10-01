##import ???

def main():
  def is_tidy(num): return num == int(''.join(sorted(str(num))))
  def maketidy(num):
    n = num
    while not is_tidy(n):
      n //= 10
      n -= 1
    bign = n*10+9
    while bign <= num:
      n = bign
      bign=bign*10+9
    return n
  
  ##f1=open(r'C:\Users\mumin\Documents\gcj\testfile.in','r')
  ##f2=open(r'C:\Users\mumin\Documents\gcj\testfile.out','w')
  ##f1=open(r'C:\Users\mumin\Documents\gcj\B-small-attempt0.in','r')
  ##f2=open(r'C:\Users\mumin\Documents\gcj\B-small-attempt0.out','w')
  f1=open(r'C:\Users\mumin\Documents\gcj\B-large.in','r')
  f2=open(r'C:\Users\mumin\Documents\gcj\B-large.out','w')
  f1.readline()
  linenum = 0
  for line in f1:
    linenum += 1
    f2.write('Case #{}: {}\n'.format(linenum,maketidy(int(line[:-1]))))
  f1.close()
  f2.close()  

if __name__ == '__main__':
  main()