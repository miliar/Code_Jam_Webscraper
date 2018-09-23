import sys

def solve(index, case):
  revd = list(str(case)[::-1])

  for _ in range(0, len(revd)-1):
    for i in range(0, len(revd)-1):
      if int(revd[i]) < int(revd[i+1]):
        for j in range(0, i+1):
          revd[j] = str(9)
        revd[i+1] = str(int(revd[i+1])-1)
   
  print('Case #{}: {}'.format(index, int(''.join(revd)[::-1])))

if __name__=='__main__':
  case_count = int(input())
  cases = [int(line) for line in sys.stdin]

  for (index, case) in zip(range(1, case_count+1), cases):
    solve(index, case)
