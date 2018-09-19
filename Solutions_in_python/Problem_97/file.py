# programing language python3
# problem: Recycled Numbers

def main():
  file_input = open('input.txt')        # reading input from this file
  file_output = open('output.txt', 'w') # this is the output file
  T = file_input.readline()
  T = int(T[:-1])
  for x in range(1,T+1):
    _S = file_input.readline()
    _S = _S.split()
    A = int(_S[0])
    B = int(_S[1])
    li = []
    y = 0
    for each in range(A, B+1):
      X= str(each)
      len = X.__len__()
      for j in range(1,len):
        s = X[j:]+X[:j]
        num = int(s)
        if (X != s) and s[0]!= '0' and num>=A and num <= B:
          n = int(X+s) if int(X)<int(s) else int(s+X)
          if n not in li:
            li.append(n)
            y += 1
    file_output.write('Case #'+str(x)+": "+str(y)+'\n')

if __name__=='__main__':
  main()
