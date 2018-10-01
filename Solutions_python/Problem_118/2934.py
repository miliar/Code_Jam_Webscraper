def issquare(apositiveint):
  
  x = apositiveint // 2
  seen = set([x])
  
  while x * x != apositiveint:
    x = (x + (apositiveint // x)) // 2
    if x in seen: return 0
    seen.add(x)
  return x

def ispalindrome(word):
    if len(word) < 2: return True
    if word[0] != word[-1]: return False
    return ispalindrome(word[1:-1])

finput = open("input.txt")
foutput = open("output.txt","w")

cases = int(finput.readline())

for case in range(cases):
    fairs = 0
    line = finput.readline()
    a, b = line.split()
    for n in range(int(a),int(b)+1):
        if n <= 1:
            fairs += 1
            continue
        if ispalindrome(str(n)):
            squaro = issquare(n)
            if squaro > 0:
                if ispalindrome(str(squaro)):
                    fairs += 1
    foutput.write("Case #"+str(case+1)+": "+str(fairs)+"\n")
    
finput.close()
foutput.close()
