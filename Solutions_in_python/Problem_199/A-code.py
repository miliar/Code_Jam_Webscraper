##import ???

def main():
  def flipp(pkstack, k):
    stack = [i == '+' for i in pkstack]
    if k > len(stack): return '0' if sum(stack) == len(stack) else 'IMPOSSIBLE'
    fnum = 0
    for i in range(len(stack)-k+1):
            if not stack[i]:
                    for j in range(k): stack[i+j] = not stack[i+j]
                    fnum += 1
    return str(fnum) if sum(stack)==len(stack) else 'IMPOSSIBLE'
  
  ##f1=open(r'C:\Users\mumin\Documents\gcj\testfile.in','r')
  ##f2=open(r'C:\Users\mumin\Documents\gcj\testfile.out','w')
  ##f1=open(r'C:\Users\mumin\Documents\gcj\A-small-attempt0.in','r')
  ##f2=open(r'C:\Users\mumin\Documents\gcj\A-small-attempt0.out','w')
  f1=open(r'C:\Users\mumin\Documents\gcj\A-large.in','r')
  f2=open(r'C:\Users\mumin\Documents\gcj\A-large.out','w')
  f1.readline()
  linenum = 0
  for line in f1:
    if not line: continue
    linenum += 1
    ind = line.find(' ')
    f2.write('Case #{}: {}\n'.format(linenum, flipp(line[:ind], int(line[ind+1:-1]))))
  f1.close()
  f2.close()

if __name__ == '__main__':
  main()