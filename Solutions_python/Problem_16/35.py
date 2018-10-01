import sys

def parseInput(fname):
  f = open(fname, 'r')
  text = f.readlines()
  f.close()

  testCases = []
  cases = int(text[0])
  cnt = 1
  for i in range(cases):
    length = int(text[cnt])
    cnt += 1
    string = text[cnt]
    cnt += 1
    testCases.append((length, string))
  return testCases


def runCase(case):
  return min(RLE(applyPermute(case[1],fix(permute))) for permute in permutations(case[0]))

def fix(permute):
  return [int(a) - 1 for a in permute]

def applyPermute(string, permute):
  k = len(permute)
  base = 0
  res = ""
  while base + k - 1 < len(string):
    for i in range(k):
      res += string[base+permute[i%k]]
    base += k
  return res

def getPermutations(a):
   if len(a)==1:
      yield a
   else:
      for i in range(len(a)):
         this = a[i]
         rest = a[:i] + a[i+1:]
         for p in getPermutations(rest):
            yield this + p

def permutations(n):
  return (permute for permute in getPermutations("".join(str(i) for i in range(1,n+1))))  

def RLE(string):
  # compute run length encoding
  curChar = string[0]
  count = 1
  for i in range(1,len(string)):
    if curChar != string[i]:
      count += 1
      curChar = string[i]
  return count

def main(inputs=["test"]):
  for inputf in inputs:
    cases = parseInput(inputf+".in")
    res = []
    i = 1
    for case in cases:
      res.append((i,runCase(case)))
      i += 1
      
    output = ["\n".join("Case #%s: %s" % (num, ans) for num,ans in res)]
    print output
    outf = open(inputf+".out",'w')
    outf.write("\n".join("Case #%s: %s" % (num, ans) for num,ans in res))
    outf.close()

if __name__=="__main__":
  if sys.argv[1:]:
    main(sys.argv[1:])
  else:
    main()
