filename = 'C-small-attempt0'
input  = open(filename+'.in')
output = open(filename+'.out','w')

T = int(input.readline().strip())

jamtext = 'welcome to code jam'

def searchfor(s,t):
  if len(s)==0:
    return 1
  count = 0

  for i in range(len(t)-len(s)+1):
    if s[0] == t[i]:
      count += searchfor(s[1:],t[i:])

  return count

for t in range(T):
  
  text = input.readline().strip()
  count = searchfor(jamtext,text)

  output.write('Case #%s: %04d\n'%(t+1,count))
